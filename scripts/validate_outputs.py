#!/usr/bin/env python3
"""Validate structured OFE decision outputs and mode-specific invariants."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from evidence_check import validate_findings

MODES = {f"MODE-{number:02d}" for number in range(1, 13)}
PERMISSIONS = {
    "READ_ONLY", "PLAN_ONLY", "IMPLEMENT_SCOPED",
    "TEST_IN_SANDBOX", "RELEASE_PREPARATION",
}
COMPLETION = {"COMPLETE", "PARTIAL", "BLOCKED", "DEFERRED", "NO_CHANGE_NEEDED"}
OSS_DECISIONS = {
    "KEEP", "REUSE_NATIVE", "INTEGRATE", "IMPROVE",
    "REPLACE", "MINIMAL_BUILD", "DEFER", "REJECT",
}
UI_UX_DECISIONS = {
    "UI_QUALITY_ACCEPTANCE_READY", "UI_QUALITY_PARTIAL",
    "UI_QUALITY_BLOCKED", "UI_QUALITY_REJECTED",
    "NO_UI_CHANGE_NEEDED", "NOT_APPLICABLE",
}
UI_UX_RESULTS = {
    "PASSED", "RISK", "UNVERIFIED", "NOT_IMPLEMENTED",
    "OUT_OF_SCOPE", "RESOLVED", "DISPUTED",
}
UI_UX_FIELDS = {
    "surface_type", "users", "core_journeys", "states", "viewports",
    "input_methods", "rendered_evidence", "functional_result",
    "visual_result", "interaction_result", "accessibility_result", "decision",
}
BASE_FIELDS = {
    "mode", "permission", "baseline", "scope", "facts", "inferences",
    "unknowns", "recommendations", "decision", "verification",
    "completion_state",
}
TASK_FIELDS = {
    "id", "owner_role", "scope", "dependencies", "acceptance",
    "rollback", "definition_of_done",
}
PLACEHOLDER = re.compile(r"(?i)(\bTBD\b|\bTODO\b|<replace[^>]*>|\{\{[^}]+\}\})")


def validate_report(data: object) -> list[str]:
    if not isinstance(data, dict):
        return ["Report must be a JSON object."]
    errors: list[str] = []
    missing = sorted(BASE_FIELDS - set(data))
    if missing:
        errors.append("missing base fields: " + ", ".join(missing))
    if data.get("mode") not in MODES:
        errors.append("mode must be MODE-01 through MODE-12")
    if data.get("permission") not in PERMISSIONS:
        errors.append("invalid permission")
    if data.get("completion_state") not in COMPLETION:
        errors.append("invalid completion_state")
    for field in ("facts", "inferences", "unknowns", "recommendations", "verification"):
        if field in data and not isinstance(data[field], list):
            errors.append(f"{field} must be a list")

    gate = data.get("open_source_gate")
    if isinstance(gate, dict) and gate.get("required"):
        if gate.get("search_status") not in {"COMPLETE", "PARTIAL", "SEARCH_UNAVAILABLE"}:
            errors.append("open_source_gate.search_status is required")
        if gate.get("decision") not in OSS_DECISIONS:
            errors.append("open_source_gate.decision is invalid")
        if not isinstance(gate.get("local_capability"), list):
            errors.append("open_source_gate.local_capability must be a list")
        if gate.get("search_status") == "SEARCH_UNAVAILABLE" and not gate.get("unknowns"):
            errors.append("SEARCH_UNAVAILABLE requires unknowns")

    ui_gate = data.get("ui_ux_gate")
    if "ui_ux_gate" in data and not isinstance(ui_gate, dict):
        errors.append("ui_ux_gate must be an object")
    elif isinstance(ui_gate, dict) and ui_gate.get("required"):
        missing_ui = sorted(UI_UX_FIELDS - set(ui_gate))
        if missing_ui:
            errors.append("ui_ux_gate missing: " + ", ".join(missing_ui))
        if not isinstance(ui_gate.get("surface_type"), str) or not ui_gate.get("surface_type"):
            errors.append("ui_ux_gate.surface_type must be non-empty")
        for field in (
            "users", "core_journeys", "states", "viewports",
            "input_methods", "rendered_evidence",
        ):
            if not isinstance(ui_gate.get(field), list) or not ui_gate.get(field):
                errors.append(f"ui_ux_gate.{field} must be a non-empty list")
        for field in (
            "functional_result", "visual_result", "interaction_result",
            "accessibility_result",
        ):
            if ui_gate.get(field) not in UI_UX_RESULTS:
                errors.append(f"ui_ux_gate.{field} is invalid")
        if ui_gate.get("decision") not in UI_UX_DECISIONS:
            errors.append("ui_ux_gate.decision is invalid")
        if ui_gate.get("decision") == "NOT_APPLICABLE":
            errors.append("a required ui_ux_gate cannot be NOT_APPLICABLE")
        if ui_gate.get("decision") in {"UI_QUALITY_ACCEPTANCE_READY", "NO_UI_CHANGE_NEEDED"}:
            result_fields = (
                "functional_result", "visual_result", "interaction_result",
                "accessibility_result",
            )
            if any(ui_gate.get(field) != "PASSED" for field in result_fields):
                errors.append("UI acceptance or no-change decisions require all four quality results to be PASSED")

    tasks = data.get("tasks", [])
    if not isinstance(tasks, list):
        errors.append("tasks must be a list")
    else:
        ids: set[str] = set()
        for index, task in enumerate(tasks):
            if not isinstance(task, dict):
                errors.append(f"tasks[{index}] must be an object")
                continue
            missing_task = sorted(TASK_FIELDS - set(task))
            if missing_task:
                errors.append(f"tasks[{index}] missing: {'', ''.join(missing_task)}")
            tid = task.get("id")
            if not isinstance(tid, str) or not tid:
                errors.append(f"tasks[{index}].id must be non-empty")
            elif tid in ids:
                errors.append(f"duplicate task id: {tid}")
            else:
                ids.add(tid)

    if "findings" in data:
        errors.extend(validate_findings({"findings": data["findings"]}))

    mode = data.get("mode")
    mode_fields = {
        "MODE-02": {"upstream_identity", "license_status"},
        "MODE-05": {"findings"},
        "MODE-07": {"deliverable_scope", "blockers", "deferred_items", "stop_work", "completion_definition"},
        "MODE-08": {"release_decision", "gates"},
        "MODE-09": {"coverage_matrix", "visual_environment", "findings"},
        "MODE-10": {"design_reference", "component_inventory", "implementation_plan", "authorization_state"},
        "MODE-11": {"baseline_capture", "comparison_capture", "diff_result", "review_classification"},
        "MODE-12": {"uat_journeys", "business_result", "role_isolation", "data_readback"},
    }
    for field in mode_fields.get(mode, set()):
        if field not in data:
            errors.append(f"{mode} requires {field}")

    rendered = json.dumps(data, ensure_ascii=False)
    if PLACEHOLDER.search(rendered):
        errors.append("unresolved placeholder detected")
    if data.get("permission") in {"READ_ONLY", "PLAN_ONLY"} and data.get("mutations_performed"):
        errors.append("read-only or plan-only output cannot report mutations_performed")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="OFE JSON report")
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}, ensure_ascii=False))
        return 2
    errors = validate_report(data)
    print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
