import tkinter as tk
from tkinter import ttk

def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

def contar_palavras_interface():
    texto = text_area.get("1.0", tk.END)
    num_palavras = contar_palavras(texto)
    label_result.config(text=f"Número de palavras: {num_palavras}")

def on_enter(e):
    button_contar.config(style="Hover.TButton")

def on_leave(e):
    button_contar.config(style="TButton")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Contador de Palavras")
root.geometry("400x300")
root.resizable(False, False)  # Desabilita maximização

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill=tk.BOTH, expand=True)

frame = ttk.Frame(root, padding="10")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Configuração da fonte
font_style = ("Helvetica", 12, "bold")

label_texto = ttk.Label(frame, text="Digite o texto:", font=font_style)
label_texto.grid(row=0, column=0, padx=5, pady=5)

text_area = tk.Text(frame, width=40, height=10, font=font_style)
text_area.grid(row=1, column=0, padx=5, pady=5)

# Estilo do botão
style = ttk.Style()
style.configure("TButton", font=font_style, borderwidth=1, relief="solid")
style.map("TButton", 
          relief=[("active", "solid"), ("pressed", "solid")],
          background=[("active", "#d9d9d9"), ("pressed", "#c0c0c0")])

# Estilo do botão quando o mouse passa sobre ele
style.configure("Hover.TButton", font=font_style, borderwidth=1, relief="solid", background="#d9d9d9")

button_contar = ttk.Button(frame, text="Contar Palavras", command=contar_palavras_interface, style="TButton")
button_contar.grid(row=2, column=0, padx=5, pady=5)

button_contar.bind("<Enter>", on_enter)
button_contar.bind("<Leave>", on_leave)

label_result = ttk.Label(frame, text="Número de palavras: 0", font=font_style)
label_result.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()