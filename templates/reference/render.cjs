// Render the reference packet HTML to PDF, then join every sheet into the Full Packet.
//   node templates/reference/render.cjs <out_dir>
// order.txt (written by build_reference.py) lists the sheet PDFs in packet order, Full Packet last.
const {chromium} = require('playwright');
const {execFileSync} = require('child_process');
const fs = require('fs'), path = require('path');
(async () => {
  const out = path.resolve(process.argv[2] || 'output/chemistry/reference');
  const order = fs.readFileSync(path.join(out, 'order.txt'), 'utf8').trim().split('\n');
  const full = order.pop();
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const pdf of order) {
    const html = path.join(out, pdf.replace(/\.pdf$/, '.html'));
    await page.goto('file://' + html);
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({path: path.join(out, pdf), preferCSSPageSize: true, printBackground: true});
    console.log('rendered', pdf);
  }
  await browser.close();
  execFileSync('pdfunite', [...order.map(p => path.join(out, p)), path.join(out, full)]);
  console.log('joined', full);
  // Only the PDFs are deliverables; the HTML and the order list are build intermediates.
  for (const pdf of order) fs.rmSync(path.join(out, pdf.replace(/\.pdf$/, '.html')), {force: true});
  fs.rmSync(path.join(out, 'order.txt'), {force: true});
})();
