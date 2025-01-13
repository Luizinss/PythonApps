import tkinter as tk
from tkinter import ttk

def is_palindrome(s):
    # Remove espaços, pontuações e converte para minúsculas
    s = ''.join(filter(str.isalnum, s)).lower()
    # Verifica se a string é igual à sua reversa
    return s == s[::-1]

def check_palindrome():
    frase = entry_frase.get()
    if is_palindrome(frase):
        label_result.config(text="É um palíndromo!")
    else:
        label_result.config(text="Não é um palíndromo.")

def create_gradient(canvas, width, height, color1, color2):
    for i in range(height):
        r1, g1, b1 = canvas.winfo_rgb(color1)
        r2, g2, b2 = canvas.winfo_rgb(color2)
        
        r = int(r1 + (r2 - r1) * i / height)
        g = int(g1 + (g2 - g1) * i / height)
        b = int(b1 + (b2 - b1) * i / height)
        
        color = f'#{r:04x}{g:04x}{b:04x}'
        
        canvas.create_line(0, i, width, i, fill=color)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Verificador de Palíndromos")
root.resizable(False, False)  # Desabilita maximização

canvas = tk.Canvas(root, width=400, height=300)
canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
create_gradient(canvas, 400, 300, "#ADD8E6", "#D8BFD8")

frame = ttk.Frame(canvas, padding="10")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label_frase = ttk.Label(frame, text="Digite uma palavra ou frase:")
label_frase.grid(row=0, column=0, padx=5, pady=5)

entry_frase = ttk.Entry(frame, width=30)
entry_frase.grid(row=1, column=0, padx=5, pady=5)

button_check = ttk.Button(frame, text="Verificar", command=check_palindrome)
button_check.grid(row=2, column=0, padx=5, pady=5)

label_result = ttk.Label(frame, text="")
label_result.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()