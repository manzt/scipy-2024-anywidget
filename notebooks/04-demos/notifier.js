if (Notification.permission === "denied") {
    await Notification.requestPermission();
}

async function dispatch(news) {
    if (!news) return;
    let { message, ...options } = news;
    if (options.icon instanceof DataView) {
        let blob = new Blob([options.icon], { type: "image/jpeg" });
        options.icon = URL.createObjectURL(blob);
    }
    if (Notification.permission === "denied") {
        await Notification.requestPermission();
    }
    let notification = new Notification(message, options);
}

export default {
    initialize({ model }) {
        model.on("change:_notification", () => dispatch(model.get("_notification")));
        dispatch(model.get("_notification"));
    },
};
