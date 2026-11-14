// Draws each page of a PDF full width, one under another, using Mozilla's PDF.js
// (assets/vendor/pdfjs-4.10.38). Markup: <div class="pdf-pages" data-pdf="file.pdf">
// with a fallback inside it; the fallback stays if the PDF cannot be drawn.
const box = document.querySelector('.pdf-pages[data-pdf]');
if (box) {
  const here = new URL(import.meta.url);
  import(new URL('vendor/pdfjs-4.10.38/pdf.min.mjs', here)).then(async pdfjs => {
    pdfjs.GlobalWorkerOptions.workerSrc = new URL('vendor/pdfjs-4.10.38/pdf.worker.min.mjs', here).href;
    const pdf = await pdfjs.getDocument(box.dataset.pdf).promise;
    const pages = [];
    for (let n = 1; n <= pdf.numPages; n++) pages.push(await pdf.getPage(n));
    let drawnWidth = 0;
    const draw = async () => {
      const width = box.clientWidth;
      if (!width || width === drawnWidth) return;
      drawnWidth = width;
      const ratio = Math.min(window.devicePixelRatio || 1, 3);
      const canvases = [];
      for (const page of pages) {
        const view = page.getViewport({ scale: width / page.getViewport({ scale: 1 }).width });
        const canvas = document.createElement('canvas');
        canvas.className = 'pdf-page';
        canvas.width = Math.floor(view.width * ratio);
        canvas.height = Math.floor(view.height * ratio);
        canvas.setAttribute('aria-hidden', 'true');
        await page.render({ canvasContext: canvas.getContext('2d'), viewport: view, transform: ratio === 1 ? null : [ratio, 0, 0, ratio, 0, 0] }).promise;
        canvases.push(canvas);
      }
      box.replaceChildren(...canvases);
      box.classList.add('is-drawn');
    };
    await draw();

    // Phones: tap a page to open it large in a scrollable view (pinch to zoom also works).
    const hint = document.createElement('p');
    hint.className = 'pdf-pages__hint';
    hint.textContent = 'Tap a page to enlarge it.';
    box.before(hint);
    const small = () => box.clientWidth < 760;
    box.addEventListener('click', event => {
      const index = [...box.children].indexOf(event.target.closest('.pdf-page'));
      if (index >= 0 && small()) openLarge(pages[index]);
    });
    const openLarge = async page => {
      const opener = document.activeElement;
      const zoom = document.createElement('div');
      zoom.className = 'pdf-zoom';
      zoom.setAttribute('role', 'dialog');
      zoom.setAttribute('aria-modal', 'true');
      zoom.setAttribute('aria-label', 'Enlarged page');
      const close = document.createElement('button');
      close.type = 'button';
      close.className = 'pdf-zoom__close';
      close.textContent = 'Close';
      const scroller = document.createElement('div');
      scroller.className = 'pdf-zoom__scroll';
      zoom.append(close, scroller);
      document.body.append(zoom);
      document.documentElement.classList.add('pdf-zoom-open');
      const shut = () => {
        zoom.remove();
        document.documentElement.classList.remove('pdf-zoom-open');
        document.removeEventListener('keydown', onKey);
        if (opener) opener.focus();
      };
      const onKey = event => { if (event.key === 'Escape') shut(); };
      close.addEventListener('click', shut);
      document.addEventListener('keydown', onKey);
      close.focus();
      const width = Math.round(Math.min(1100, Math.max(720, window.innerWidth * 1.9)));
      const ratio = Math.min(window.devicePixelRatio || 1, 2);
      const view = page.getViewport({ scale: width / page.getViewport({ scale: 1 }).width });
      const canvas = document.createElement('canvas');
      canvas.className = 'pdf-zoom__page';
      canvas.width = Math.floor(view.width * ratio);
      canvas.height = Math.floor(view.height * ratio);
      canvas.style.width = width + 'px';
      canvas.setAttribute('aria-hidden', 'true');
      await page.render({ canvasContext: canvas.getContext('2d'), viewport: view, transform: ratio === 1 ? null : [ratio, 0, 0, ratio, 0, 0] }).promise;
      scroller.append(canvas);
    };

    let timer;
    window.addEventListener('resize', () => { clearTimeout(timer); timer = setTimeout(draw, 250); });
  }).catch(() => {});
}
