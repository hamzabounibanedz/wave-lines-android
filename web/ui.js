export const $ = selector => document.querySelector(selector);
let timer;
export function message(text) {
  $('#message').textContent = text;
  clearTimeout(timer);
  timer = setTimeout(() => { $('#message').textContent = ''; }, 4800);
}
export function read(key, initial) {
  try { return JSON.parse(localStorage.getItem(key)) ?? initial; }
  catch { return initial; }
}
export function save(key, value) {
  try { localStorage.setItem(key, JSON.stringify(value)); }
  catch { message('Browser storage is unavailable. Changes will last for this session.'); }
}
export function download(canvas, name) {
  canvas.toBlob(blob => {
    if (!blob) { message('The image could not be exported.'); return; }
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a'); link.href=url; link.download=name; link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1500);
  }, 'image/png');
}

