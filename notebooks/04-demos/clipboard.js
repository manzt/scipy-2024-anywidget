// read and write data from clipboard
export default {
    initialize({ model }) {
        document.addEventListener("copy", () => {
            model.set("value", window.getSelection().toString());
            model.save_changes();
        });
        model.on("change:value", () => {
            navigator.clipboard.writeText(model.get("value"));
        });
    },
    render({ model, el }) {
        el.innerHTML = `<pre>${model.get("value")}</pre>`;
        model.on("change:value", () => {
            el.innerHTML = `<pre>${model.get("value")}</pre>`;
        });
    },
};
