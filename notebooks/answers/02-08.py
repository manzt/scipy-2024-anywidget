# Exercise 8 Solution

class StyledWidgetAnswer(anywidget.AnyWidget):
    _esm = """
    export function render({ model, el }) {
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
        el.classList.add("styled-widget-answer");
    }
    export default { render };
    """
    _css = """
    .styled-widget-answer button {
        background: linear-gradient(
            300deg,
            #9933ff 33.26%,
            #ff6666 46.51%,
            #faca30 59.77%,
            #00cd99 73.03%,
            #00ccff 86.29%
        );
        border-radius: 10px;
        border: 0;
        color: white;
        cursor: pointer;
        font-family: "Roboto", sans-serif;
        font-size: 2em;
        margin: 10px;
        padding: 10px 20px;
        transition: transform 0.25s ease-in-out;
    }
    .styled-widget-answer button:hover {
        transform: scale(1.05);
    }
    """
    count = traitlets.Int(0).tag(sync=True)

StyledWidgetAnswer()
