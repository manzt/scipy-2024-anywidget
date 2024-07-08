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
  console.log(model.get("_bytes"));
  const btn = document.createElement("button");
  btn.innerText = "It's me Mario!";
  btn.addEventListener("click", () => {
    chime({ duration: model.get("duration"), tone1: model.get("tone1"), tone2: model.get("tone2") });
  });
  model.on("msg:custom", (msg) => {
    if (msg?.kind === "click") btn.click();
  });
  el.appendChild(btn);
}

export default { render };