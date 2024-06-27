# Exercise 1 Solution

class Widget(anywidget.AnyWidget):
    _esm = """
    function render() {
      console.log("Hello from anywidget!");
    }
    export deafult { render }
    """

Widget()
