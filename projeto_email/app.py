from flask import Flask, request, render_template, jsonify
import PyPDF2

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = ""
    # Lendo o texto do formulário
    if "text" in request.form:
        text = request.form["text"]

    # Lendo arquivos enviados
    if "file" in request.files:
        file = request.files["file"]
        fname = file.filename.lower()
        if fname.endswith(".txt"):
            text = file.read().decode("utf-8", errors="ignore")
        elif fname.endswith(".pdf"):
            reader = PyPDF2.PdfReader(file)
            pages = []
            for p in reader.pages:
                t = p.extract_text() or ""
                pages.append(t)
            text = "".join(pages)

    # Classificação simplificada
    if any(word in text.lower() for word in ["trabalho", "projeto", "solicito"]):
        category = "Produtivo"
        reply = "Obrigado pelo envio, vamos dar andamento ao seu pedido."
    else:
        category = "Não Produtivo"
        reply = "Mensagem recebida, não requer ação imediata."

    return jsonify({"category": category, "reply": reply})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)

