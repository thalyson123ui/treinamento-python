import tkinter as tk

def criar_tabuada(n):
    resultado = ""
    for i in range(1, 11):
        resultado += f"{n} x {i} = {n*i}\n"
    return resultado

def mostrar_tabuada():
    for widget in frame.winfo_children():
        widget.destroy()
    for n in range(2, 11):
        label = tk.Label(frame, text=criar_tabuada(n), font=('Arial', 12), padx=10, pady=10, borderwidth=2, relief="groove")
        label.pack(side="left", expand=True, padx=5)

root = tk.Tk()
root.title("Tabuadas do 2 ao 10")
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

botao = tk.Button(root, text="Mostrar Tabuadas", command=mostrar_tabuada)
botao.pack(pady=10)

root.mainloop()