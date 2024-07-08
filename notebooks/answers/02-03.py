# Exercise 3 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    function render({ model, el }) {
        const h1 = document.createElement("h1");
        h1.innerText = `Hello, ${model.get("name")}!`;
        el.appendChild(h1);
    }
    export default { render };
    """
    name = traitlets.Unicode().tag(sync=True)

Widget(name="World")
