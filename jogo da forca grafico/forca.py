import tkinter as tk
from tkinter import messagebox
import random

# Lista de palavras para o jogo
PALAVRAS = ["CARRO", "MOTO", "LANCHA", "TENIS", "PISTA"]

class JogoForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        
        self.palavra_secreta = random.choice(PALAVRAS)
        self.palavra_oculta = ["_" for _ in self.palavra_secreta]
        self.tentativas_restantes = 6
        self.letras_erradas = set()
        
        self.label_palavra = tk.Label(root, text=" ".join(self.palavra_oculta), font=("Arial", 20))
        self.label_palavra.pack(pady=10)
        
        self.label_tentativas = tk.Label(root, text=f"Tentativas restantes: {self.tentativas_restantes}", font=("Arial", 14))
        self.label_tentativas.pack()
        
        self.frame_teclado = tk.Frame(root)
        self.frame_teclado.pack()
        
        self.botoes = {}
        for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            btn = tk.Button(self.frame_teclado, text=letra, width=4, height=2, command=lambda l=letra: self.tentar_letra(l))
            btn.grid(row=(ord(letra) - ord('A')) // 7, column=(ord(letra) - ord('A')) % 7)
            self.botoes[letra] = btn
        
    def tentar_letra(self, letra):
        if letra in self.palavra_secreta:
            for i, l in enumerate(self.palavra_secreta):
                if l == letra:
                    self.palavra_oculta[i] = letra
            self.label_palavra.config(text=" ".join(self.palavra_oculta))
        else:
            self.tentativas_restantes -= 1
            self.letras_erradas.add(letra)
            self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas_restantes}")
        
        self.botoes[letra].config(state=tk.DISABLED)
        
        self.verificar_fim()
        
    def verificar_fim(self):
        if "_" not in self.palavra_oculta:
            messagebox.showinfo("Jogo da Forca", "Parabéns! Você venceu!")
            self.root.quit()
        elif self.tentativas_restantes == 0:
            messagebox.showinfo("Jogo da Forca", f"Você perdeu! A palavra era {self.palavra_secreta}")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    JogoForca(root)
    root.mainloop()
