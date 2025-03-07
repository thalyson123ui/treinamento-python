import tkinter as tk
from tkinter import messagebox
import sqlite3

# Configuração do banco de dados
conn = sqlite3.connect("biblioteca.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano INTEGER NOT NULL)''')
conn.commit()

# Funções
def adicionar_livro():
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    ano = entrada_ano.get()
    if titulo and autor and ano:
        c.execute("INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)", (titulo, autor, ano))
        conn.commit()
        entrada_titulo.delete(0, tk.END)
        entrada_autor.delete(0, tk.END)
        entrada_ano.delete(0, tk.END)
        listar_livros()
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos")

def listar_livros():
    lista.delete(0, tk.END)
    c.execute("SELECT * FROM livros")
    for livro in c.fetchall():
        lista.insert(tk.END, f"{livro[1]} - {livro[2]} ({livro[3]})")

def buscar_livro():
    lista.delete(0, tk.END)
    titulo = entrada_titulo.get()
    c.execute("SELECT * FROM livros WHERE titulo LIKE ?", (f"%{titulo}%",))
    for livro in c.fetchall():
        lista.insert(tk.END, f"{livro[1]} - {livro[2]} ({livro[3]})")

def remover_livro():
    selecionado = lista.curselection()
    if selecionado:
        livro_texto = lista.get(selecionado)
        titulo = livro_texto.split(" - ")[0]
        c.execute("DELETE FROM livros WHERE titulo = ?", (titulo,))
        conn.commit()
        listar_livros()
    else:
        messagebox.showwarning("Erro", "Selecione um livro para remover")

# Interface gráfica
janela = tk.Tk()
janela.title("Biblioteca Virtual")
janela.geometry("400x400")

# Campos de entrada
tk.Label(janela, text="Título").pack()
entrada_titulo = tk.Entry(janela)
entrada_titulo.pack()

tk.Label(janela, text="Autor").pack()
entrada_autor = tk.Entry(janela)
entrada_autor.pack()

tk.Label(janela, text="Ano").pack()
entrada_ano = tk.Entry(janela)
entrada_ano.pack()

# Botões
tk.Button(janela, text="Adicionar Livro", command=adicionar_livro).pack()
tk.Button(janela, text="Buscar Livro", command=buscar_livro).pack()
tk.Button(janela, text="Remover Livro", command=remover_livro).pack()
tk.Button(janela, text="Listar Todos", command=listar_livros).pack()

# Lista de livros
lista = tk.Listbox(janela)
lista.pack(expand=True, fill=tk.BOTH)
listar_livros()

janela.mainloop()

# Fechando conexão com o banco de dados
conn.close()
