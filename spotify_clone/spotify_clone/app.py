import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'spotify-secret-key'

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'mp3'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Cria pasta se não existir
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    songs = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', songs=songs)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('Nenhum arquivo enviado.')
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        flash('Nenhum arquivo selecionado.')
        return redirect(url_for('index'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Upload feito com sucesso!')
        return redirect(url_for('index'))
    else:
        flash('Tipo de arquivo não permitido. Apenas .mp3')
        return redirect(url_for('index'))

@app.route('/play/<filename>')
def play_song(filename):
    return render_template('player.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)