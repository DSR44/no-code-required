import { chromium } from 'playwright';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

(async () => {
  const htmlPath = path.join(__dirname, 'source.html');
  const pdfPath = path.join(__dirname, 'the-0-dollar-ai-starter-kit.pdf');
  const apiAssetPath = path.join(__dirname, '../../api/assets/the-0-dollar-ai-starter-kit.pdf');

  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });
  await page.pdf({
    path: pdfPath,
    format: 'Letter',
    printBackground: true,
    margin: { top: '0.5in', bottom: '0.75in', left: '0.65in', right: '0.65in' },
  });
  await browser.close();

  const fs = await import('fs');
  fs.mkdirSync(path.dirname(apiAssetPath), { recursive: true });
  fs.copyFileSync(pdfPath, apiAssetPath);
  console.log('PDF created:', pdfPath);
  console.log('Copied to:', apiAssetPath);
})();
