# Example 4 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
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
      const btn = document.createElement("button");
      btn.innerText = "It's me Mario!";
      btn.addEventListener("click", () => {
        chime({ duration: model.get("duration"), gain: model.get("gain") });
      });
      model.on("msg:custom", (msg) => {
        if (msg?.kind === "click") btn.click();
      });
      el.appendChild(btn);
    }
    export default { render };
    """
    duration = traitlets.Float(1.0).tag(sync=True)
    gain = traitlets.Float(0.1).tag(sync=True)

    def click(self):
        self.send({ "kind": "click" })

widget = Widget()
widget
