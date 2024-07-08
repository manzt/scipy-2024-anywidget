# Exercise 2 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    function render({ el }) {
      const h1 = document.createElement("h1");
      h1.innerHTML = "Hello, anywidget!";
      el.appendChild(h1);
    }
    export default { render };
    """

Widget()
