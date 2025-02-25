import tkinter as tk
from tkinter import messagebox
import datetime

# Função para determinar a geração
def determinar_geracao():
    try:
        ano_nascimento = int(entrada_idade.get())
        ano_atual = datetime.datetime.now().year
        idade = ano_atual - ano_nascimento
        
        if 1997 <= ano_nascimento <= 2012:
            geracao = "Geração Z"
        elif 1981 <= ano_nascimento <= 1996:
            geracao = "Millennials"
        elif 1965 <= ano_nascimento <= 1980:
            geracao = "Geração X"
        elif 1946 <= ano_nascimento <= 1964:
            geracao = "Baby Boomers"
        elif 1928 <= ano_nascimento <= 1945:
            geracao = "Geração Silenciosa"
        else:
            geracao = "Fora das categorias definidas"
        
        resultado_label.config(text=f"Você pertence à {geracao}", fg="blue")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um ano válido.")

# Criando a interface gráfica
root = tk.Tk()
root.title("Analisador de Geração")
root.geometry("300x200")

label_instrucao = tk.Label(root, text="Digite seu ano de nascimento:")
label_instrucao.pack(pady=5)

entrada_idade = tk.Entry(root)
entrada_idade.pack(pady=5)

botao_verificar = tk.Button(root, text="Verificar Geração", command=determinar_geracao)
botao_verificar.pack(pady=5)

resultado_label = tk.Label(root, text="", font=("Arial", 12))
resultado_label.pack(pady=5)

root.mainloop()
