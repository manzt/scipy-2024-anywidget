# Excercise 4 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    export function render({ model, el }) {
        const btn = document.createElement("button");
        btn.innerText = `Count is ${model.get("count")}`;
        el.appendChild(btn);
    }
    """
    count = traitlets.Int(0).tag(sync=True)

Widget()
