# Visual Tooling and Capability Discovery

Never claim a browser, accessibility scanner, screenshot-diff engine, or desktop automation result merely because the tool is commonly available. Discover the current environment first and record version, executable or package identity, permission, and actual exit or connection result.

## Preferred reuse order

1. Existing project browser tests, component harnesses, visual baselines, and CI artifacts.
2. Installed browser automation and developer tools.
3. Installed screenshot capture, image comparison, and accessibility tools.
4. Installed desktop UI automation for native or WebView flows.
5. A reviewed additional dependency only when existing capability cannot satisfy the frozen acceptance conditions and installation is authorized.

## Capability record

Record each capability as `AVAILABLE`, `UNAVAILABLE`, `BLOCKED`, or `UNVERIFIED`, with:

- tool and version or resolved package identity;
- executable or controlled surface;
- supported browser, desktop host, or operating system;
- whether it can capture screenshots, console, network, accessibility, input, and native windows;
- data, credential, profile, download, or paid-service side effects;
- evidence command and result;
- gaps that remain manual or UNVERIFIED.

## Current OFE-003 development environment

The 2026-10-27 isolated upgrade environment verified installed Node Playwright and `playwright-core`, `pixelmatch`, `pngjs`, `sharp`, Google Chrome, Microsoft Edge, Python Pillow, and Codex Computer Use browser and Windows desktop automation. It did not find `@playwright/test`, `axe-core`, `@axe-core/playwright`, Python Playwright, Selenium, pywinauto, OpenCV, imagehash, ImageMagick, or ffmpeg.

This inventory is environment-specific evidence, not a portability promise. When axe or an equivalent scanner is unavailable, record automated accessibility coverage as unavailable and perform applicable semantic, focus, keyboard, zoom, contrast, and assistive checks without claiming an axe pass.

The included `scripts/visual_runtime_probe.cjs` is an optional isolated fixture probe. It uses already installed Playwright, pixelmatch, and pngjs; it does not install packages, access business projects, or convert its deterministic signals into a release decision by itself.
