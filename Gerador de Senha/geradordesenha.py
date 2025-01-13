import tkinter as tk
from tkinter import ttk
import random
import string

def gerar_senha(tamanho=12):
    # Definindo os caracteres que podem ser usados na senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gerando a senha aleatória
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    
    return senha

def gerar_senha_interface():
    try:
        tamanho = int(entry_tamanho.get())
        senha = gerar_senha(tamanho)
        label_result.config(text=f"Sua senha gerada é: {senha}")
    except ValueError:
        label_result.config(text="Por favor, insira um valor numérico válido.")

def copiar_senha():
    senha = label_result.cget("text").replace("Sua senha gerada é: ", "")
    root.clipboard_clear()
    root.clipboard_append(senha)
    root.update()  # Mantém a área de transferência atualizada
    label_copiar.config(text="Senha copiada!")

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
root.title("Gerador de Senha Aleatória")
root.resizable(False, False)  # Desabilita maximização

canvas = tk.Canvas(root, width=400, height=300)
canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
create_gradient(canvas, 400, 300, "#8A2BE2", "#4B0082")

frame = ttk.Frame(canvas, padding="10")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label_tamanho = ttk.Label(frame, text="Digite o tamanho da senha desejada:")
label_tamanho.grid(row=0, column=0, padx=5, pady=5)

entry_tamanho = ttk.Entry(frame, width=30)
entry_tamanho.grid(row=1, column=0, padx=5, pady=5)

button_gerar = ttk.Button(frame, text="Gerar Senha", command=gerar_senha_interface)
button_gerar.grid(row=2, column=0, padx=5, pady=5)

label_result = ttk.Label(frame, text="")
label_result.grid(row=3, column=0, padx=5, pady=5)

button_copiar = ttk.Button(frame, text="Copiar Senha", command=copiar_senha)
button_copiar.grid(row=4, column=0, padx=5, pady=5)

label_copiar = ttk.Label(frame, text="")
label_copiar.grid(row=5, column=0, padx=5, pady=5)

root.mainloop()