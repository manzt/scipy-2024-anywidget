import pathlib

import anywidget
import traitlets


class Notifier(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "notifier.js"
    _notification = traitlets.Dict(None, allow_none=True).tag(sync=True)

    def notify(
        self, message: str, *, body: str | None = None, image: str | bytes | None = None
    ):
        self._notification = {"message": message, "body": body, "icon": image}


class Detector(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "detector.js"
    height = traitlets.Int(150).tag(sync=True)
    detections = traitlets.List().tag(sync=True)
    color = traitlets.Unicode("red").tag(sync=True)
    landmark_color = traitlets.Unicode("blue").tag(sync=True)
    kind = traitlets.Enum(["face", "barcode"], default_value="barcode").tag(sync=True)


class Clipboard(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "clipboard.js"
    value = traitlets.Unicode().tag(sync=True)
