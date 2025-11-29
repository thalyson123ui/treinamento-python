from flask import Flask, render_template, session, redirect, url_for, request, flash
from decimal import Decimal
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret")  # troque em produção

# Catálogo simples (em produção, use banco de dados)
PRODUTOS = {
    1: {"id": 1, "nome": "Camiseta Minimal", "preco": Decimal("79.90"), "descricao": "Algodão, corte unissex.", "imagem": "https://images.pexels.com/photos/991509/pexels-photo-991509.jpeg"},
    2: {"id": 2, "nome": "Tênis Urban", "preco": Decimal("249.00"), "descricao": "Conforto diário.", "imagem": "https://images.pexels.com/photos/34945394/pexels-photo-34945394.jpeg"},
    3: {"id": 3, "nome": "Mochila Tech", "preco": Decimal("189.50"), "descricao": "Compartimentos e resistência.", "imagem": "https://images.pexels.com/photos/3731256/pexels-photo-3731256.jpeg"},
}

def get_carrinho():
    carrinho = session.get("carrinho", {})
    # garantir estrutura {produto_id: {qty, nome, preco}}
    return carrinho

def salvar_carrinho(carrinho):
    session["carrinho"] = carrinho
    session.modified = True

def subtotal_carrinho(carrinho):
    return sum(Decimal(item["preco"]) * item["qty"] for item in carrinho.values())

@app.route("/")
def index():
    return render_template("index.html", produtos=list(PRODUTOS.values()))

@app.route("/produto/<int:produto_id>")
def produto(produto_id):
    prod = PRODUTOS.get(produto_id)
    if not prod:
        flash("Produto não encontrado.")
        return redirect(url_for("index"))
    return render_template("produto.html", produto=prod)

@app.route("/adicionar/<int:produto_id>", methods=["POST"])
def adicionar(produto_id):
    prod = PRODUTOS.get(produto_id)
    if not prod:
        flash("Produto inválido.")
        return redirect(url_for("index"))

    try:
        qty = int(request.form.get("qty", "1"))
        if qty < 1:
            qty = 1
    except ValueError:
        qty = 1

    carrinho = get_carrinho()
    key = str(produto_id)
    if key in carrinho:
        carrinho[key]["qty"] += qty
    else:
        carrinho[key] = {
            "id": produto_id,
            "nome": prod["nome"],
            "preco": str(prod["preco"]),  # sessão não serializa Decimal
            "qty": qty,
        }
    salvar_carrinho(carrinho)
    flash(f"{qty}x {prod['nome']} adicionado(s) ao carrinho.")
    return redirect(url_for("carrinho"))

@app.route("/carrinho")
def carrinho():
    carrinho = get_carrinho()
    total = subtotal_carrinho(carrinho)
    return render_template("carrinho.html", carrinho=carrinho, total=total)

@app.route("/atualizar", methods=["POST"])
def atualizar():
    carrinho = get_carrinho()
    for key, item in list(carrinho.items()):
        qty_str = request.form.get(f"qty_{key}", "")
        try:
            qty = int(qty_str)
            if qty <= 0:
                carrinho.pop(key)
            else:
                item["qty"] = qty
        except ValueError:
            # ignora entradas inválidas
            pass
    salvar_carrinho(carrinho)
    flash("Carrinho atualizado.")
    return redirect(url_for("carrinho"))

@app.route("/remover/<int:produto_id>", methods=["POST"])
def remover(produto_id):
    carrinho = get_carrinho()
    key = str(produto_id)
    if key in carrinho:
        carrinho.pop(key)
        salvar_carrinho(carrinho)
        flash("Item removido.")
    return redirect(url_for("carrinho"))

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    carrinho = get_carrinho()
    if request.method == "POST":
        # Simulação de pagamento
        if not carrinho:
            flash("Seu carrinho está vazio.")
            return redirect(url_for("index"))
        nome = request.form.get("nome")
        email = request.form.get("email")
        endereco = request.form.get("endereco")
        if not (nome and email and endereco):
            flash("Preencha todos os campos.")
            return redirect(url_for("checkout"))

        total = subtotal_carrinho(carrinho)
        # Aqui você integraria com um gateway (ex.: Stripe, Mercado Pago)
        session.pop("carrinho", None)
        flash(f"Pedido confirmado! Total: R$ {total:.2f}")
        return redirect(url_for("index"))

    total = subtotal_carrinho(carrinho)
    return render_template("checkout.html", carrinho=carrinho, total=total)

if __name__ == "__main__":
    app.run(debug=True)