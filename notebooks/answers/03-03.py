# Exercise 3 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    function chime({ duration, tone1, tone2 }) { // <---- NEW!
      const c = new AudioContext();
      const g = c.createGain();
      const o = c.createOscillator();
      g.connect(c.destination);
      g.gain.value = 0.1;
      g.gain.linearRampToValueAtTime(0, duration); // <---- NEW!
      o.connect(g);
      o.type = "square";
      o.frequency.setValueAtTime(tone1, 0); // <---- NEW!
      o.frequency.setValueAtTime(tone2, 0.08); // <---- NEW!
      o.start();
      o.stop(duration); // <---- NEW!
    }
    function render({ model, el }) {
      const btn = document.createElement("button");
      btn.innerText = "It's me Mario!";
      btn.addEventListener("click", () => {
        chime({ duration: model.get("duration"), tone1: model.get("tone1"), tone2: model.get("tone2") }); // <---- NEW!
      });
      el.appendChild(btn);
    }
    export default { render };
    """
    duration = traitlets.Float(1.0).tag(sync=True)
                             # ^ provide a default value
    tone1 = traitlets.Int(988).tag(sync=True)
                        # ^ provide a default value
    tone2 = traitlets.Int(1319).tag(sync=True)
                        # ^ provide a default value

widget = Widget()
widget

