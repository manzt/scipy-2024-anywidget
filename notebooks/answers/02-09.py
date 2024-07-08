# Exercise 9

class ConfettiWidget(anywidget.AnyWidget):
    _esm = """
    import confetti from "https://esm.sh/canvas-confetti@1";

    function render({ model, el }) {
        const btn = document.createElement("button");
        btn.innerText = `Count is ${model.get("count")}`;
        btn.addEventListener("click", () => {
            model.set("count", model.get("count") + 1);
            model.save_changes();
        });
        model.on("change:count", () => {
            confetti({ angle: model.get("count") * 10 });
            btn.innerText = `Count is ${model.get("count")}`;
        });
        el.appendChild(btn);
    }
    export default { render };
    """
    count = traitlets.Int(0).tag(sync=True)

ConfettiWidget()
