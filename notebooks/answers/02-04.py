# Excercise 4 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    function render({ model, el }) {
        const btn = document.createElement("button");
        btn.innerText = `Count is ${model.get("count")}`;
        el.appendChild(btn);
    }
    export default { render };
    """
    count = traitlets.Int(0).tag(sync=True)

Widget()
