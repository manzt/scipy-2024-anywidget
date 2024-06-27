# Excercise 5 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    export function render({ model, el }) {
        const btn = document.createElement("button");
        btn.innerText = `Count is ${model.get("count")}`;
        btn.addEventListener("click", () => {
          console.log("clicked");
        });
        el.appendChild(btn);
    }
    """
    count = traitlets.Int().tag(sync=True)

Widget()
