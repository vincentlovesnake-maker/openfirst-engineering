import json
import os
import shutil
import socket
import subprocess
import sys
import time
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "visual_runtime"


def free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def wait_for_port(port, timeout=8):
    deadline = time.time() + timeout
    while time.time() < deadline:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if sock.connect_ex(("127.0.0.1", port)) == 0:
                return
        time.sleep(0.05)
    raise TimeoutError(f"fixture server did not open port {port}")


class VisualRuntimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.environ.get("OFE_RUN_VISUAL_RUNTIME") != "1":
            raise unittest.SkipTest("set OFE_RUN_VISUAL_RUNTIME=1 for the optional real-browser fixture")
        cls.node = os.environ.get("OFE_NODE") or shutil.which("node")
        cls.browser = os.environ.get("OFE_BROWSER_EXECUTABLE")
        cls.node_modules = os.environ.get("OFE_NODE_MODULES")
        if not cls.node or not Path(cls.node).exists():
            raise unittest.SkipTest("Node executable is unavailable")
        if not cls.browser or not Path(cls.browser).exists():
            raise unittest.SkipTest("OFE_BROWSER_EXECUTABLE is unavailable")
        if not cls.node_modules or not Path(cls.node_modules).exists():
            raise unittest.SkipTest("OFE_NODE_MODULES is unavailable")

        cls.output = Path(
            os.environ.get("OFE_VISUAL_EVIDENCE_DIR", ROOT / "tmp" / "visual-runtime")
        ).resolve()
        if cls.output.exists():
            shutil.rmtree(cls.output)
        cls.output.mkdir(parents=True)
        cls.port = free_port()
        cls.closed_port = free_port()
        env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
        cls.server = subprocess.Popen(
            [sys.executable, str(FIXTURE / "server.py"), "--port", str(cls.port)],
            cwd=FIXTURE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
        try:
            wait_for_port(cls.port)
            result_file = cls.output / "runtime-result.json"
            run_env = {
                **os.environ,
                "NODE_PATH": cls.node_modules,
                "OFE_BROWSER_EXECUTABLE": cls.browser,
                "TMP": str(cls.output),
                "TEMP": str(cls.output),
            }
            cls.probe = subprocess.run(
                [
                    cls.node,
                    str(ROOT / "scripts" / "visual_runtime_probe.cjs"),
                    "--base", f"http://127.0.0.1:{cls.port}",
                    "--unreachable", f"http://127.0.0.1:{cls.closed_port}/missing",
                    "--output", str(cls.output),
                    "--result", str(result_file),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=60,
                env=run_env,
            )
            if cls.probe.returncode != 0:
                raise AssertionError(cls.probe.stdout + cls.probe.stderr)
            cls.result = json.loads(result_file.read_text(encoding="utf-8"))
        except Exception:
            cls.server.terminate()
            cls.server.wait(timeout=5)
            raise

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, "server") and cls.server.poll() is None:
            cls.server.terminate()
            try:
                cls.server.wait(timeout=5)
            except subprocess.TimeoutExpired:
                cls.server.kill()
                cls.server.wait(timeout=5)

    def test_normal_page_has_real_save_and_no_invented_finding(self):
        case = self.result["cases"]["normal"]
        self.assertEqual(case["status"], "PASSED")
        self.assertEqual(case["persisted"], "verified-user")
        self.assertIsNone(case["finding"])

    def test_overflow_is_detected_from_runtime_geometry(self):
        case = self.result["cases"]["overflow"]
        self.assertEqual(case["status"], "CONFIRMED")
        self.assertEqual(case["findingType"], "LAYOUT")
        self.assertGreater(case["geometry"]["scrollWidth"], case["geometry"]["innerWidth"])

    def test_dom_only_success_is_not_business_success(self):
        case = self.result["cases"]["brokenAction"]
        self.assertEqual(case["status"], "CONFIRMED")
        self.assertEqual(case["findingType"], "BUSINESS_FLOW")
        self.assertEqual(case["saveRequestCount"], 0)
        self.assertEqual(case["persistedAfterReload"], "")

    def test_reference_capture_yields_plan_without_claiming_implementation(self):
        case = self.result["cases"]["designReference"]
        self.assertEqual(case["status"], "PLAN_READY")
        self.assertGreater(len(case["implementationPlan"]), 0)
        self.assertFalse(case["implementationClaimed"])

    def test_shared_component_regression_has_retained_diff(self):
        case = self.result["cases"]["sharedRegression"]
        self.assertEqual(case["status"], "CONFIRMED")
        self.assertGreater(case["diff"]["changedPixels"], 0)
        self.assertTrue(Path(case["diff"]["diffPath"]).exists())

    def test_unreachable_environment_is_unverified(self):
        case = self.result["cases"]["unreachable"]
        self.assertEqual(case["status"], "UNVERIFIED")
        self.assertTrue(case["navigationError"])

    def test_asset_url_change_is_not_mislabeled_as_design_defect(self):
        case = self.result["cases"]["assetVersion"]
        self.assertFalse(case["designDefect"])
        self.assertEqual(case["findingType"], "DEPLOYMENT_ASSET")
        self.assertEqual(case["diff"]["changedPixels"], 0)
        self.assertGreaterEqual(len(case["requestedAssets"]), 2)

    def test_accessibility_tool_gap_is_disclosed(self):
        coverage = self.result["automatedAccessibility"]
        self.assertEqual(coverage["status"], "UNAVAILABLE")
        self.assertIn("axe-core", coverage["reason"])


if __name__ == "__main__":
    unittest.main()
