if (Notification.permission !== "denied") {
    await Notification.requestPermission();
}
export default {
    initialize({ model, el }) {
        model.on("change:_notification", async () => {
            console.log("hello");
            let { message, ...options } = model.get("_notification");
            if (options.icon instanceof DataView) {
                let blob = new Blob([options.icon], { type: "image/jpeg" });
                options.icon = URL.createObjectURL(blob);
            }
            if (Notification.permission !== "denied") {
                await Notification.requestPermission();
            }
            // options.tag = `notification-${Date.now()}`;
            let notification = new Notification(message, options);
            console.log(notification);
        });
    },
};
