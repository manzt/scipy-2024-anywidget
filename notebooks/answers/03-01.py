# Exercise 1 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    function chime() {
      const c = new AudioContext();
      const g = c.createGain();
      const o = c.createOscillator();
      g.connect(c.destination);
      g.gain.value = 0.1;
      g.gain.linearRampToValueAtTime(0, 1);
      o.connect(g);
      o.type = "square";
      o.frequency.setValueAtTime(988, 0);
      o.frequency.setValueAtTime(1319, 0.08);
      o.start();
      o.stop(1);
    }
    function render() {
        chime();
    }
    export default { render };
    """

Widget()