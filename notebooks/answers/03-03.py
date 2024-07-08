# Exercise 3 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    function chime({ duration, gain }) { // <---- NEW!
      let c = new AudioContext();
      let g = c.createGain();
      let o = c.createOscillator();
      let of = o.frequency;
      g.connect(c.destination);
      g.gain.value = gain; // <---- NEW!
      g.gain.linearRampToValueAtTime(0, duration); // <---- NEW!
      o.connect(g);
      o.type = "square";
      of.setValueAtTime(988, 0);
      of.setValueAtTime(1319, 0.08);
      o.start();
      o.stop(duration); // <---- NEW!
    }
    function render({ model, el }) {
      const btn = document.createElement("button");
      btn.innerText = "It's me Mario!";
      btn.addEventListener("click", () => {
        chime({ duration: model.get("duration"), gain: model.get("gain") }); // <---- NEW!
      });
      el.appendChild(btn);
    }
    export default { render };
    """
    duration = traitlets.Float(1.0).tag(sync=True)
                             # ^ provide a default value
    gain = traitlets.Float(0.1).tag(sync=True)
                         # ^ provide a default value

widget = Widget()
widget
