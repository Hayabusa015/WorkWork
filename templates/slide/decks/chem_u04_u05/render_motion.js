/* Render a frame-deterministic motion HTML (it must expose render(t)) to MP4.
 *
 *   node render_motion.js motion_polarity.html out.mp4 [seconds=16] [fps=30]
 *   node render_motion.js motion_polarity.html still.png --still 15.5
 *
 * Each frame is a screenshot at an exact time, so the video does not depend on how fast
 * the browser happened to run. Frames are piped straight into ffmpeg.
 */
const { chromium } = require("playwright");
const { spawn } = require("child_process");
const path = require("path");

(async () => {
  const [src, out, a3, a4] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await page.goto("file://" + path.resolve(src));
  await page.evaluate(() => document.fonts.ready);
  if (a3 === "--still") {
    await page.evaluate((t) => render(t), parseFloat(a4));
    await page.screenshot({ path: out });
    await browser.close();
    return;
  }
  const secs = parseFloat(a3 || "16"), fps = parseInt(a4 || "30", 10);
  const ff = spawn("ffmpeg", ["-y", "-v", "error", "-f", "image2pipe", "-framerate", String(fps), "-i", "-",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-movflags", "+faststart", out],
    { stdio: ["pipe", "inherit", "inherit"] });
  const n = Math.round(secs * fps);
  for (let i = 0; i < n; i++) {
    await page.evaluate((t) => render(t), i / fps);
    const buf = await page.screenshot({ type: "png" });
    if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once("drain", r));
  }
  ff.stdin.end();
  await new Promise((r) => ff.on("close", r));
  await browser.close();
  console.log(`wrote ${out}: ${n} frames`);
})();
