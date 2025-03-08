import tkinter as tk
from tkinter import ttk, messagebox

# Dicionário de tradução simples (exemplo)
dicionario_traducao = {
    "Olá": {"en": "Hello", "es": "Hola", "fr": "Bonjour", "de": "Hallo"},
    "Mundo": {"en": "World", "es": "Mundo", "fr": "Monde", "de": "Welt"},
    "Bom dia": {"en": "Good morning", "es": "Buenos días", "fr": "Bonjour", "de": "Guten Morgen"},
}

# Idiomas suportados
idiomas_disponiveis = {
    "Português": "pt",
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Alemão": "de"
}

def traduzir():
    texto = entrada_texto.get("1.0", tk.END).strip()
    idioma_destino = idiomas_disponiveis.get(combo_destino.get(), "en")
    
    if not texto:
        messagebox.showwarning("Aviso", "Digite um texto para traduzir!")
        return
    
    palavras = texto.split()
    resultado = " ".join([dicionario_traducao.get(palavra, {}).get(idioma_destino, palavra) for palavra in palavras])
    
    saida_texto.delete("1.0", tk.END)
    saida_texto.insert(tk.END, resultado)

# Criando a janela principal
janela = tk.Tk()
janela.title("Tradutor")
janela.geometry("500x400")
janela.resizable(False, False)

# Widgets
label_destino = ttk.Label(janela, text="Idioma de destino:")
label_destino.pack(pady=5)
combo_destino = ttk.Combobox(janela, values=list(idiomas_disponiveis.keys()))
combo_destino.pack(pady=5)
combo_destino.set("Inglês")

entrada_texto = tk.Text(janela, height=5, width=50)
entrada_texto.pack(pady=10)

botao_traduzir = ttk.Button(janela, text="Traduzir", command=traduzir)
botao_traduzir.pack(pady=5)

saida_texto = tk.Text(janela, height=5, width=50, state=tk.NORMAL)
saida_texto.pack(pady=10)

# Iniciar a interface
janela.mainloop()
