# Exercise 2 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    function chime() {
      let c = new AudioContext();
      let g = c.createGain();
      let o = c.createOscillator();
      let of = o.frequency;
      g.connect(c.destination);
      g.gain.value = 0.1;
      g.gain.linearRampToValueAtTime(0, 1);
      o.connect(g);
      o.type = "square";
      of.setValueAtTime(988, 0);
      of.setValueAtTime(1319, 0.08);
      o.start();
      o.stop(1);
    }
    function render({ el }) {
      const btn = document.createElement("button");
      btn.innerText = "It's me Mario!";
      btn.addEventListener("click", () => {
        chime();
      });
      el.appendChild(btn);
    }
    export default { render };
    """

Widget()
