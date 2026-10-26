#!/usr/bin/env python3
"""Isolated HTTP fixture for OFE visual and UAT runtime tests."""

from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse


STATE = {"value": ""}

COMMON_STYLE = """
* { box-sizing: border-box; }
html, body { margin: 0; min-height: 100%; font-family: Arial, sans-serif; color: #172033; background: #f5f7fa; }
main { width: min(720px, calc(100% - 32px)); margin: 36px auto; }
.panel { background: #fff; border: 1px solid #d9dee8; padding: 24px; border-radius: 8px; }
label { display: block; margin: 16px 0 6px; font-weight: 700; }
input { width: 100%; min-height: 42px; padding: 8px 10px; border: 1px solid #8792a5; }
button { min-height: 42px; margin-top: 12px; padding: 8px 16px; border: 0; color: #fff; background: #1769aa; font-weight: 700; cursor: pointer; }
button:focus, input:focus { outline: 3px solid #f0a000; outline-offset: 2px; }
#status { min-height: 24px; margin-top: 12px; }
"""


def page(title: str, body: str, extra_style: str = "", script: str = "", head: str = "") -> bytes:
    html = (
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>{title}</title>{head}<style>{COMMON_STYLE}{extra_style}</style></head>"
        f"<body>{body}<script>{script}</script></body></html>"
    )
    return html.encode("utf-8")


class Handler(BaseHTTPRequestHandler):
    server_version = "OFEVisualFixture/1.0"

    def log_message(self, format_string: str, *args: object) -> None:
        return

    def send_bytes(self, payload: bytes, content_type: str, status: int = 200) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/api/state":
            self.send_bytes(json.dumps(STATE).encode("utf-8"), "application/json")
            return
        if path == "/assets/app.css":
            css = b".asset-box{width:360px;padding:24px;background:#fff;border:2px solid #1769aa;color:#172033}"
            self.send_bytes(css, "text/css")
            return
        if path == "/normal":
            script = """
const input = document.querySelector('#value');
const status = document.querySelector('#status');
async function loadState() {
  const response = await fetch('/api/state');
  const data = await response.json();
  input.value = data.value || '';
}
document.querySelector('#save').addEventListener('click', async () => {
  const response = await fetch('/api/save', {
    method: 'POST', headers: {'content-type': 'application/json'},
    body: JSON.stringify({value: input.value})
  });
  status.textContent = response.ok ? 'Saved' : 'Failed';
  status.dataset.state = response.ok ? 'done' : 'failed';
});
loadState();
"""
            body = (
                "<main><section class='panel'><h1>Account preference</h1>"
                "<label for='value'>Display name</label><input id='value'>"
                "<button id='save' type='button'>Save</button>"
                "<p id='status' role='status' aria-live='polite'></p></section></main>"
            )
            self.send_bytes(page("Normal", body, script=script), "text/html")
            return
        if path == "/overflow":
            body = (
                "<main><section class='panel'><h1>Wide report</h1>"
                "<div id='wide-panel'>This fixed panel exceeds the approved viewport.</div></section></main>"
            )
            style = "#wide-panel{width:1200px;padding:20px;background:#ffe9e9;border:2px solid #b42318}"
            self.send_bytes(page("Overflow", body, extra_style=style), "text/html")
            return
        if path == "/broken-action":
            body = (
                "<main><section class='panel'><h1>Profile</h1>"
                "<label for='value'>Display name</label><input id='value'>"
                "<button id='save' type='button'>Save</button>"
                "<p id='status' role='status'></p></section></main>"
            )
            script = """
document.querySelector('#save').addEventListener('click', () => {
  const status = document.querySelector('#status');
  status.textContent = 'Saved';
  status.dataset.state = 'done';
});
"""
            self.send_bytes(page("Broken action", body, script=script), "text/html")
            return
        if path in {"/reference-design", "/reference-target"}:
            reference = path == "/reference-design"
            body = (
                "<main><section class='panel' id='design-panel'><h1>Workspace</h1>"
                "<p>Review queued work and continue the primary task.</p>"
                "<button type='button'>Continue</button></section></main>"
            )
            if reference:
                style = (
                    "#design-panel{padding:32px;border-radius:6px;border-color:#a9b4c5}"
                    "#design-panel h1{font-size:30px;color:#172033}"
                    "#design-panel button{background:#1769aa;border-radius:4px}"
                )
            else:
                style = (
                    "#design-panel{padding:14px;border-radius:18px;border-color:#d8bfd8}"
                    "#design-panel h1{font-size:22px;color:#6b2c91}"
                    "#design-panel button{background:#777;border-radius:18px}"
                )
            self.send_bytes(page("Design reference", body, extra_style=style), "text/html")
            return
        if path in {"/shared-before", "/shared-after"}:
            after = path == "/shared-after"
            body = (
                "<header class='shared-nav'><strong>Workspace</strong><nav>Home &nbsp; Queue</nav></header>"
                "<main><section class='panel'><h1>Queue</h1><p>Shared navigation regression fixture.</p></section></main>"
            )
            height = 88 if after else 56
            style = (
                f".shared-nav{{height:{height}px;display:flex;align-items:center;justify-content:space-between;"
                "padding:0 24px;background:#172033;color:#fff}}"
            )
            self.send_bytes(page("Shared component", body, extra_style=style), "text/html")
            return
        if path in {"/asset-v1", "/asset-v2"}:
            version = "1" if path.endswith("v1") else "2"
            head = f"<link rel='stylesheet' href='/assets/app.css?v={version}'>"
            body = "<main><div class='asset-box'><h1>Stable asset rendering</h1><p>The URL changes; the CSS bytes do not.</p></div></main>"
            self.send_bytes(page("Asset version", body, head=head), "text/html")
            return
        self.send_bytes(b"not found", "text/plain", 404)

    def do_POST(self) -> None:
        if urlparse(self.path).path != "/api/save":
            self.send_bytes(b"not found", "text/plain", 404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        try:
            body = json.loads(self.rfile.read(length).decode("utf-8"))
            STATE["value"] = str(body.get("value", ""))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self.send_bytes(b'{"ok":false}', "application/json", 400)
            return
        self.send_bytes(b'{"ok":true}', "application/json")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, required=True)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
