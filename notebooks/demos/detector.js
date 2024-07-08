function draw(canvas, { detections, color, landmarkColor }) {
    let context = canvas.getContext("2d");
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.strokeStyle = color;
    context.lineWidth = 3;
    context.beginPath();
    for (let { boundingBox: bbox, landmarks = [] } of detections) {
        context.rect(bbox.x, bbox.y, bbox.width, bbox.height);
        context.stroke();

        context.fillStyle = landmarkColor;
        context.lineWidth = 2;
        for (let landmark of landmarks) {
            for (let point of landmark.locations) {
                context.beginPath();
                context.arc(point.x, point.y, 2, 0, 2 * Math.PI);
                context.fill();
            }
        }
    }
}

let formats = await BarcodeDetector.getSupportedFormats();
function createDetector(kind) {
    if (kind === "face") {
        return new window.FaceDetector();
    }
    return new BarcodeDetector({ formats });
}

async function render({ model, el }) {
    // Setup
    let detector = await createDetector(model.get("kind"));
    let stream = await navigator.mediaDevices?.getUserMedia({
        video: { facingMode: "environment" },
    });

    // Create the video element
    let video = Object.assign(document.createElement("video"), {
        autoplay: true,
        srcObject: stream,
    });
    video.style.display = "block";
    video.style.transform = "scaleX(-1)";
    video.style.borderRadius = "10px"; // Rounded corners

    // Create the canvas element for drawing bounding boxes
    let canvas = document.createElement("canvas");
    canvas.style.position = "absolute";
    canvas.style.top = "0";
    canvas.style.left = "0";
    canvas.style.transform = "scaleX(-1)";
    canvas.style.pointerEvents = "none";

    let div = document.createElement("div");
    div.style.position = "relative";
    div.appendChild(video);
    div.appendChild(canvas);

    // Center and append the video element
    el.style.position = "relative";
    el.style.display = "grid";
    el.style.placeItems = "center";
    el.appendChild(div);

    // Update the canvas on any state change
    model.on("change", () => {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        draw(canvas, {
            detections: model.get("detections"),
            color: model.get("color"),
            landmarkColor: model.get("landmark_color"),
        });
    });

    // Change the detector on kind change
    model.on("change:kind", async () => {
        detector = await createDetector(model.get("kind"));
    });

    let running = true;
    async function detect() {
        if (!running) return;
        let update = await detector.detect(video).catch(() => []);
        model.set("detections", update);
        model.save_changes();
        requestAnimationFrame(detect);
    }
    requestAnimationFrame(detect);
    return () => {
        running = false;
        stream.getTracks().forEach((track) => track.stop());
    };
}

export default { render };
