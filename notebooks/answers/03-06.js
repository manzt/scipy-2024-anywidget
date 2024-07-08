function chime({ duration, tone1, tone2 }) {
  const c = new AudioContext();
  const g = c.createGain();
  const o = c.createOscillator();
  g.connect(c.destination);
  g.gain.value = 0.1;
  g.gain.linearRampToValueAtTime(0, duration);
  o.connect(g);
  o.type = "square";
  o.frequency.setValueAtTime(tone1, 0);
  o.frequency.setValueAtTime(tone2, 0.08);
  o.start();
  o.stop(duration);
}

function render({ model, el }) {
  const canvas = document.createElement("canvas");

  canvas.width = 16;
  canvas.height = 16;
  canvas.style.width = "30px"
  canvas.style.height = "30px";

  const bytes = new Uint8ClampedArray(
    model.get("_bytes").buffer,
  );
  const imgData = new ImageData(bytes, 16, 16);
  const ctx = canvas.getContext("2d");
  ctx.putImageData(imgData, 0, 0);
    
  canvas.innerText = "It's me Mario!";
  canvas.addEventListener("click", () => {
    chime({ duration: model.get("duration"), tone1: model.get("tone1"), tone2: model.get("tone2") });
  });
  model.on("msg:custom", (msg) => {
    if (msg?.kind === "click") canvas.click();
  });
  el.appendChild(canvas);
}

export default { render };