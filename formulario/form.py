import tkinter as tk
from tkinter import messagebox

def enviar():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    if not nome or not email or not telefone:
        messagebox.showwarning("aviso", "todos os campos devem ser preenchidos")
        return
    
    # exibir os dados no terminal
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Telefone: {telefone}")

    # exibir menssagem de sucesso
    messagebox.showinfo("Sucesso", "Dados enviados com sucesso")

    # limpar oa campos
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

# criar a janela principal
root = tk.Tk()
root.title("Formulário de contato")
root.geometry("300x200")

# criar os widgets
label_nome = tk.Label(root, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

label_telefone = tk.Label(root, text="Telefone:")
label_telefone.pack()
entry_telefone = tk.Entry(root)
entry_telefone.pack()

button_enviar = tk.Button(root, text="Enviar", command=enviar)
button_enviar.pack()

# executar o loop principal
tk.mainloop()