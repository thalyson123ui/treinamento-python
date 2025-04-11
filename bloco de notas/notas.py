from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Lista que vai armazenar as notas em memória
notas = []
contador_id = 1  # para atribuir IDs únicos

# HTML básico
template_html = """
<!doctype html>
<html>
<head>
    <title>Bloco de Notas</title>
</head>
<body>
    <h1>Bloco de Notas</h1>
    <form action="{{ url_for('add_nota') }}" method="post">
        <textarea name="texto" rows="4" cols="50" placeholder="Escreva sua nota aqui..."></textarea><br>
        <button type="submit">Adicionar Nota</button>
    </form>
    <ul>
    {% for nota in notas %}
        <li>
            {{ nota.texto }}
            <a href="{{ url_for('delete_nota', nota_id=nota.id) }}">[Deletar]</a>
        </li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(template_html, notas=notas)

@app.route('/add', methods=['POST'])
def add_nota():
    global contador_id
    texto = request.form.get('texto', '').strip()
    if texto:
        notas.append({"id": contador_id, "texto": texto})
        contador_id += 1
    return redirect(url_for('index'))

@app.route('/delete/<int:nota_id>')
def delete_nota(nota_id):
    global notas
    notas = [n for n in notas if n["id"] != nota_id]
    return redirect(url_for('index'))

# Para rodar localmente:
# if __name__ == '__main__':
#     app.run(debug=True)
