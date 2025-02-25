import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        
        if imc < 18.5:
            resultado = "Abaixo do peso"
            cor = "blue"
        elif 18.5 <= imc < 25:
            resultado = "Peso normal"
            cor = "green"
        elif 25 <= imc < 30:
            resultado = "Sobrepeso"
            cor = "orange"
        else:
            resultado = "Obesidade"
            cor = "red"
        
        label_resultado.config(text=f"IMC: {imc:.2f} - {resultado}", fg=cor)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x200")

# Labels e Entradas
tk.Label(janela, text="Peso (kg):").pack()
entry_peso = tk.Entry(janela)
entry_peso.pack()

tk.Label(janela, text="Altura (m):").pack()
entry_altura = tk.Entry(janela)
entry_altura.pack()

# Botão de cálculo
btn_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
btn_calcular.pack()

# Label de resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Executando a interface
janela.mainloop()