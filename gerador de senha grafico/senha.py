import tkinter as tk
import string
import random
import threading
import time

def generate_password():
    try:
        length = int(length_var.get())
        if length < 4:
            print("Aviso: A senha deve ter pelo menos 4 caracteres.")
            return
        
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        password_var.set(password)
        animate_label()
    except ValueError:
        print("Erro: Por favor, insira um número válido.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    print("Senha copiada para a área de transferência!")

def animate_label():
    def animation():
        colors = ["red", "blue", "green", "purple", "orange"]
        for _ in range(10):
            password_label.config(fg=random.choice(colors))
            time.sleep(0.1)
        password_label.config(fg="black")
    threading.Thread(target=animation, daemon=True).start()

# Criando a janela principal
root = tk.Tk()
root.title("Gerador de Senha")
root.geometry("400x300")
root.resizable(False, False)

# Variáveis
length_var = tk.StringVar(value="12")
password_var = tk.StringVar()

# Layout
tk.Label(root, text="Comprimento da Senha:").pack(pady=5)
length_entry = tk.Entry(root, textvariable=length_var, width=5)
length_entry.pack()

generate_button = tk.Button(root, text="Gerar Senha", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, textvariable=password_var, font=("Arial", 14, "bold"))
password_label.pack(pady=10)

copy_button = tk.Button(root, text="Copiar", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Rodando o loop da interface
root.mainloop()
