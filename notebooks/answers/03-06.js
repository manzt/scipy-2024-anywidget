function chime({ duration, gain }) {
  let c = new AudioContext();
  let g = c.createGain();
  let o = c.createOscillator();
  let of = o.frequency;
  g.connect(c.destination);
  g.gain.value = gain;
  g.gain.linearRampToValueAtTime(0, duration);
  o.connect(g);
  o.type = "square";
  of.setValueAtTime(988, 0);
  of.setValueAtTime(1319, 0.08);
  o.start();
  o.stop(duration);
}

function render({ model, el }) {
  const size = "30px";
  const canvas = document.createElement("canvas");
  canvas.width = 16;
  canvas.height = 16;
  canvas.style.width = size;
  canvas.style.height = size;
  const bytes = new Uint8ClampedArray(
    model.get("_box").buffer,
  );
  const imgData = new ImageData(bytes, 16, 16);
  const ctx = canvas.getContext("2d");
  ctx.putImageData(imgData, 0, 0);
    
  canvas.addEventListener("click", () => {
    chime({ duration: model.get("duration"), gain: model.get("gain") });
  });
  model.on("msg:custom", (msg) => {
    if (msg?.kind === "click") canvas.click();
  });
  el.appendChild(canvas);
}
export default { render };
