import tkinter as tk
from tkinter import messagebox
import random

# Lista de perguntas e respostas
perguntas = [
    {"pergunta": "Qual é a capital do Brasil?", "opcoes": ["São Paulo", "Brasília", "Rio de Janeiro", "Salvador"], "resposta": "Brasília"},
    {"pergunta": "Quem pintou a Mona Lisa?", "opcoes": ["Van Gogh", "Leonardo da Vinci", "Picasso", "Michelangelo"], "resposta": "Leonardo da Vinci"},
    {"pergunta": "Qual é o maior planeta do sistema solar?", "opcoes": ["Terra", "Júpiter", "Saturno", "Marte"], "resposta": "Júpiter"},
]

# Inicializa o jogo
def iniciar_jogo():
    global pergunta_atual, score
    pergunta_atual = 0
    score = 0
    mostrar_pergunta()

def mostrar_pergunta():
    global pergunta_atual
    if pergunta_atual < len(perguntas):
        p = perguntas[pergunta_atual]
        if "pergunta" in p and "opcoes" in p and "resposta" in p and isinstance(p["opcoes"], list) and len(p["opcoes"]) == 4:
            lbl_pergunta.config(text=p["pergunta"])
            for i in range(4):
                botoes[i].config(text=p["opcoes"][i], command=lambda opcao=p["opcoes"][i]: verificar_resposta(opcao))
        else:
            print(f"Erro na pergunta {pergunta_atual}: {p}")
            messagebox.showerror("Erro", "Pergunta mal formatada.")
    else:
        messagebox.showinfo("Fim de jogo", f"Você ganhou {score} pontos!")

def verificar_resposta(opcao):
    global pergunta_atual, score
    if opcao == perguntas[pergunta_atual].get("resposta", ""):
        score += 1
    pergunta_atual += 1
    mostrar_pergunta()

# Criando a interface gráfica
root = tk.Tk()
root.title("Show do Milhão")
root.geometry("500x400")

lbl_pergunta = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
lbl_pergunta.pack(pady=20)

botoes = []
for i in range(4):
    btn = tk.Button(root, text="", width=40, height=2, font=("Arial", 12))
    btn.pack(pady=5)
    botoes.append(btn)

btn_iniciar = tk.Button(root, text="Iniciar Jogo", command=iniciar_jogo, font=("Arial", 14))
btn_iniciar.pack(pady=20)

root.mainloop()
