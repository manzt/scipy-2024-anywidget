# Exercise 7 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    function render({ model, el }) {
        const btn = document.createElement("button");
        btn.innerText = `Count is ${model.get("count")}`;
        btn.addEventListener("click", () => {
            model.set("count", model.get("count") + 1);
            model.save_changes();
        });
        model.on("change:count", () => {
            btn.innerText = `Count is ${model.get("count")}`;
        });
        el.appendChild(btn);
    }
    export default { render };
    """
    count = traitlets.Int().tag(sync=True)

widget = Widget()
widget
