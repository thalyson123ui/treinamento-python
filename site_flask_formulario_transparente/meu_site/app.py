from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        print(f"Recebido: {nome}, {email}")
        return f"Obrigado, {nome}! Seu email ({email}) foi recebido."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
