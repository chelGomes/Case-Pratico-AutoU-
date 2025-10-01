const form = document.getElementById("emailForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);

    const response = await fetch("/analyze", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    resultDiv.innerHTML = `<strong>Categoria:</strong> ${data.category}<br><strong>Resposta:</strong> ${data.reply}`;
});
