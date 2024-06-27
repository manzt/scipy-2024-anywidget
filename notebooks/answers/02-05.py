# Excercise 5 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    function render({ model, el }) {
        const btn = document.createElement("button");
        btn.innerText = `Count is ${model.get("count")}`;
        btn.addEventListener("click", () => {
          console.log("clicked");
        });
        el.appendChild(btn);
    }
    export default { render };
    """
    count = traitlets.Int().tag(sync=True)

Widget()
