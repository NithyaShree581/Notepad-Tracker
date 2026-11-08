
const filenameInput = document.getElementById("filename");
const editor = document.getElementById("editor");
const saveStatus = document.getElementById("save-status");

document.getElementById("save-btn").addEventListener("click", async () => {
    const filename = filenameInput.value.trim();

    if (!filename) {
        saveStatus.textContent = "Enter a filename";
        return;
    }

    try {
        const response = await fetch("/api/files", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                filename: filename,
                content: editor.value
            })
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "Save failed");
        }

        saveStatus.textContent = "File saved successfully";
    } catch (error) {
        saveStatus.textContent = error.message;
    }
});

document.getElementById("open-btn").addEventListener("click", async () => {
    const filename = filenameInput.value.trim();

    if (!filename) {
        saveStatus.textContent = "Enter a filename";
        return;
    }

    try {
        const response = await fetch(
            `/api/files?filename=${encodeURIComponent(filename)}`
        );

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "Open failed");
        }

        editor.value = result.content;
        saveStatus.textContent = "File opened successfully";
    } catch (error) {
        saveStatus.textContent = error.message;
    }
});
