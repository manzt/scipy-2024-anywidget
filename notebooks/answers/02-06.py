# Excercise 6 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    export function render({ model, el }) {
        const btn = document.createElement("button");
        btn.innerText = `Count is ${model.get("count")}`;
        btn.addEventListener("click", () => {
            model.set("count", model.get("count") + 1);
            model.save_changes();
        });
        el.appendChild(btn);
    }
    """
    count = traitlets.Int().tag(sync=True)

widget = Widget()
widget
