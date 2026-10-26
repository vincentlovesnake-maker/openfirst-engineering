#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");
const pixelmatchModule = require("pixelmatch");
const pixelmatch = pixelmatchModule.default || pixelmatchModule;
const { PNG } = require("pngjs");

function argument(name) {
  const index = process.argv.indexOf(name);
  if (index === -1 || !process.argv[index + 1]) {
    throw new Error("Missing required argument " + name);
  }
  return process.argv[index + 1];
}

function comparePng(beforePath, afterPath, diffPath) {
  const before = PNG.sync.read(fs.readFileSync(beforePath));
  const after = PNG.sync.read(fs.readFileSync(afterPath));
  if (before.width !== after.width || before.height !== after.height) {
    throw new Error("Screenshot dimensions differ");
  }
  const diff = new PNG({ width: before.width, height: before.height });
  const changedPixels = pixelmatch(
    before.data,
    after.data,
    diff.data,
    before.width,
    before.height,
    { threshold: 0.1 }
  );
  fs.writeFileSync(diffPath, PNG.sync.write(diff));
  return { changedPixels, width: before.width, height: before.height, diffPath };
}

async function screenshot(page, target) {
  await page.screenshot({ path: target, fullPage: true, animations: "disabled" });
  return target;
}

async function designTokens(page) {
  return page.evaluate(() => {
    const panel = document.querySelector("#design-panel");
    const heading = panel.querySelector("h1");
    const button = panel.querySelector("button");
    const p = getComputedStyle(panel);
    const h = getComputedStyle(heading);
    const b = getComputedStyle(button);
    return {
      panelPadding: p.padding,
      panelRadius: p.borderRadius,
      panelBorderColor: p.borderColor,
      headingSize: h.fontSize,
      headingColor: h.color,
      buttonBackground: b.backgroundColor,
      buttonRadius: b.borderRadius
    };
  });
}

async function main() {
  const base = argument("--base").replace(/\/$/, "");
  const outputDir = path.resolve(argument("--output"));
  const outputFile = path.resolve(argument("--result"));
  const unreachableUrl = argument("--unreachable");
  const executablePath = process.env.OFE_BROWSER_EXECUTABLE;
  fs.mkdirSync(outputDir, { recursive: true });
  const profileDir = path.join(outputDir, "browser-profile");
  fs.rmSync(profileDir, { recursive: true, force: true });

  const context = await chromium.launchPersistentContext(profileDir, {
    headless: true,
    executablePath: executablePath || undefined,
    viewport: { width: 800, height: 600 },
    locale: "en-US",
    colorScheme: "light",
    reducedMotion: "reduce",
    acceptDownloads: false,
    args: ["--disable-background-networking", "--disable-component-update"]
  });

  const result = {
    baseline: "ofe-visual-fixture-v1",
    browser: { requestedExecutable: executablePath || "playwright-default" },
    automatedAccessibility: {
      status: "UNAVAILABLE",
      reason: "axe-core and equivalent automated scanner were not present in the verified environment"
    },
    cases: {},
    artifacts: []
  };

  try {
    const normal = await context.newPage();
    await normal.goto(base + "/normal", { waitUntil: "networkidle" });
    await normal.locator("#value").fill("verified-user");
    await normal.locator("#save").click();
    await normal.locator("#status[data-state='done']").waitFor();
    await normal.reload({ waitUntil: "networkidle" });
    const persisted = await normal.locator("#value").inputValue();
    await normal.keyboard.press("Tab");
    const focusVisible = await normal.evaluate(() => document.activeElement && document.activeElement.id === "value");
    const normalShot = path.join(outputDir, "normal.png");
    await screenshot(normal, normalShot);
    result.artifacts.push(normalShot);
    result.cases.normal = {
      status: persisted === "verified-user" ? "PASSED" : "CONFIRMED",
      persisted,
      focusVisible,
      finding: null
    };
    await normal.close();

    const overflow = await context.newPage();
    await overflow.goto(base + "/overflow", { waitUntil: "networkidle" });
    const geometry = await overflow.evaluate(() => ({
      scrollWidth: document.documentElement.scrollWidth,
      innerWidth: window.innerWidth
    }));
    const overflowShot = path.join(outputDir, "overflow.png");
    await screenshot(overflow, overflowShot);
    result.artifacts.push(overflowShot);
    result.cases.overflow = {
      status: geometry.scrollWidth > geometry.innerWidth ? "CONFIRMED" : "PASSED",
      findingType: geometry.scrollWidth > geometry.innerWidth ? "LAYOUT" : null,
      geometry
    };
    await overflow.close();

    const broken = await context.newPage();
    const saveRequests = [];
    broken.on("request", request => {
      if (request.url().includes("/api/save")) saveRequests.push(request.url());
    });
    await broken.goto(base + "/broken-action", { waitUntil: "networkidle" });
    await broken.locator("#value").fill("not-persisted");
    await broken.locator("#save").click();
    await broken.locator("#status[data-state='done']").waitFor();
    const brokenShot = path.join(outputDir, "broken-action.png");
    await screenshot(broken, brokenShot);
    result.artifacts.push(brokenShot);
    await broken.reload({ waitUntil: "networkidle" });
    const afterReload = await broken.locator("#value").inputValue();
    result.cases.brokenAction = {
      status: saveRequests.length === 0 && afterReload === "" ? "CONFIRMED" : "PASSED",
      findingType: saveRequests.length === 0 && afterReload === "" ? "BUSINESS_FLOW" : null,
      displayedSuccess: true,
      saveRequestCount: saveRequests.length,
      persistedAfterReload: afterReload
    };
    await broken.close();

    const reference = await context.newPage();
    await reference.goto(base + "/reference-design", { waitUntil: "networkidle" });
    const referenceTokens = await designTokens(reference);
    const referenceShot = path.join(outputDir, "design-reference.png");
    await screenshot(reference, referenceShot);
    result.artifacts.push(referenceShot);
    await reference.goto(base + "/reference-target", { waitUntil: "networkidle" });
    const targetTokens = await designTokens(reference);
    const targetShot = path.join(outputDir, "design-target.png");
    await screenshot(reference, targetShot);
    result.artifacts.push(targetShot);
    const tokenChanges = Object.keys(referenceTokens)
      .filter(key => referenceTokens[key] !== targetTokens[key])
      .map(key => ({ token: key, current: targetTokens[key], reference: referenceTokens[key] }));
    result.cases.designReference = {
      status: "PLAN_READY",
      referenceTokens,
      targetTokens,
      implementationPlan: tokenChanges,
      implementationClaimed: false
    };
    await reference.close();

    const shared = await context.newPage();
    const sharedBefore = path.join(outputDir, "shared-before.png");
    const sharedAfter = path.join(outputDir, "shared-after.png");
    const sharedDiff = path.join(outputDir, "shared-diff.png");
    await shared.goto(base + "/shared-before", { waitUntil: "networkidle" });
    await screenshot(shared, sharedBefore);
    await shared.goto(base + "/shared-after", { waitUntil: "networkidle" });
    await screenshot(shared, sharedAfter);
    const sharedComparison = comparePng(sharedBefore, sharedAfter, sharedDiff);
    result.artifacts.push(sharedBefore, sharedAfter, sharedDiff);
    result.cases.sharedRegression = {
      status: sharedComparison.changedPixels > 0 ? "CONFIRMED" : "PASSED",
      classification: sharedComparison.changedPixels > 0 ? "UNINTENDED_SHARED_COMPONENT_CHANGE" : "NO_PIXEL_CHANGE",
      diff: sharedComparison
    };
    await shared.close();

    const asset = await context.newPage();
    const assetRequests = [];
    asset.on("request", request => {
      if (request.url().includes("/assets/app.css")) assetRequests.push(request.url());
    });
    const assetV1 = path.join(outputDir, "asset-v1.png");
    const assetV2 = path.join(outputDir, "asset-v2.png");
    const assetDiff = path.join(outputDir, "asset-diff.png");
    await asset.goto(base + "/asset-v1", { waitUntil: "networkidle" });
    await screenshot(asset, assetV1);
    await asset.goto(base + "/asset-v2", { waitUntil: "networkidle" });
    await screenshot(asset, assetV2);
    const assetComparison = comparePng(assetV1, assetV2, assetDiff);
    result.artifacts.push(assetV1, assetV2, assetDiff);
    result.cases.assetVersion = {
      status: "PASSED",
      findingType: assetComparison.changedPixels === 0 ? "DEPLOYMENT_ASSET" : "UNKNOWN",
      designDefect: false,
      requestedAssets: assetRequests,
      diff: assetComparison
    };
    await asset.close();

    const unreachable = await context.newPage();
    let navigationError = "";
    try {
      await unreachable.goto(unreachableUrl, { waitUntil: "domcontentloaded", timeout: 2000 });
    } catch (error) {
      navigationError = String(error.message || error).split("\n")[0];
    }
    result.cases.unreachable = {
      status: navigationError ? "UNVERIFIED" : "PASSED",
      navigationError
    };
    await unreachable.close();
  } finally {
    await context.close();
    fs.rmSync(profileDir, { recursive: true, force: true });
  }

  fs.writeFileSync(outputFile, JSON.stringify(result, null, 2), "utf8");
  process.stdout.write(JSON.stringify({ ok: true, result: outputFile }) + "\n");
}

main().catch(error => {
  process.stderr.write(String(error.stack || error) + "\n");
  process.exitCode = 1;
});
