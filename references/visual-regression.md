# MODE-11 VISUAL_REGRESSION

Use this mode to determine whether a UI change produced intended or unintended rendered effects. Typical permission is `TEST_IN_SANDBOX`.

## Equivalent comparison contract

Freeze before and after:

- source commit, build, artifact, asset manifest, feature flags, and deployment identity;
- browser or desktop host and version, viewport or DPI, zoom, locale, fonts, color scheme, motion setting, and operating system where material;
- route, role, account, data, time-dependent content, loading completion, animation state, and cache or service-worker state;
- baseline owner, approval, capture command, file hash, and expected change region.

If these conditions are not equivalent, classify the comparison as non-equivalent or `UNVERIFIED`; do not convert the pixel count into a product conclusion.

## Required workflow

1. Capture baseline and candidate evidence under the frozen contract.
2. Use available image comparison to locate changed regions and record threshold and dimensions.
3. Review each region against the approved design and business scope.
4. Classify it as expected design change, unintended visual regression, functional or data difference, environment or rendering difference, or unresolved.
5. Operate affected controls and shared components; a visually identical image does not prove functional equivalence.
6. Sample other routes that share the changed component, token, stylesheet, layout shell, or asset pipeline.
7. Retain baseline, candidate, diff, metadata, and review decision. Do not update the baseline merely to make the test pass.

Pixel difference is evidence, not the quality decision. Asset URL or hash changes with identical rendering belong to deployment or asset analysis, not a design defect. Use [../assets/visual-regression-template.md](../assets/visual-regression-template.md).
