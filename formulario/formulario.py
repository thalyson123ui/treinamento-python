from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template embutido com formulário
form_template = '''
<!doctype html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title>Formulário Flask</title>
  </head>
  <body>
    <h1>Formulário de Contato</h1>
    <form method="POST">
      <label for="nome">Nome:</label><br>
      <input type="text" id="nome" name="nome" required><br><br>
      <label for="email">Email:</label><br>
      <input type="email" id="email" name="email" required><br><br>
      <input type="submit" value="Enviar">
    </form>

    {% if nome and email %}
    <h2>Dados Recebidos:</h2>
    <p><strong>Nome:</strong> {{ nome }}</p>
    <p><strong>Email:</strong> {{ email }}</p>
    {% endif %}
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def formulario():
    nome = email = None
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
    return render_template_string(form_template, nome=nome, email=email)

if __name__ == '__main__':
    app.run(debug=True)
