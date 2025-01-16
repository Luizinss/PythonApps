import tkinter as tk
from tkinter import ttk
import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo"]
    return random.choice(palavras)

def exibir_palavra_oculta(palavra, letras_adivinhadas):
    return " ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra])

def iniciar_jogo():
    global palavra, letras_adivinhadas, tentativas, partes_boneco
    palavra = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6
    partes_boneco = 0
    atualizar_interface()
    canvas.delete("boneco")
    button_verificar.config(state=tk.NORMAL)

def atualizar_interface():
    palavra_oculta = exibir_palavra_oculta(palavra, letras_adivinhadas)
    label_palavra.config(text=palavra_oculta)
    label_tentativas.config(text=f"Tentativas restantes: {tentativas}")

def verificar_letra():
    global tentativas, partes_boneco
    letra = entry_letra.get().lower()
    entry_letra.delete(0, tk.END)

    if letra in letras_adivinhadas:
        label_mensagem.config(text="Você já adivinhou essa letra.")
    elif letra in palavra:
        letras_adivinhadas.append(letra)
        label_mensagem.config(text="Boa! Você adivinhou uma letra.")
    else:
        tentativas -= 1
        partes_boneco += 1
        desenhar_boneco(partes_boneco)
        label_mensagem.config(text=f"Letra errada. Você tem {tentativas} tentativas restantes.")

    if all(letra in letras_adivinhadas for letra in palavra):
        label_mensagem.config(text=f"Parabéns! Você adivinhou a palavra: {palavra}")
        button_verificar.config(state=tk.DISABLED)
    elif tentativas == 0:
        label_mensagem.config(text=f"Você perdeu! A palavra era: {palavra}")
        button_verificar.config(state=tk.DISABLED)

    atualizar_interface()

def desenhar_boneco(partes):
    if partes == 1:
        canvas.create_oval(350, 50, 400, 100, tags="boneco")  # Cabeça
    elif partes == 2:
        canvas.create_line(375, 100, 375, 200, tags="boneco")  # Corpo
    elif partes == 3:
        canvas.create_line(375, 120, 325, 170, tags="boneco")  # Braço esquerdo
    elif partes == 4:
        canvas.create_line(375, 120, 425, 170, tags="boneco")  # Braço direito
    elif partes == 5:
        canvas.create_line(375, 200, 325, 250, tags="boneco")  # Perna esquerda
    elif partes == 6:
        canvas.create_line(375, 200, 425, 250, tags="boneco")  # Perna direita

def create_gradient(canvas, width, height, color1, color2):
    for i in range(height):
        r1, g1, b1 = canvas.winfo_rgb(color1)
        r2, g2, b2 = canvas.winfo_rgb(color2)
        
        r = int(r1 + (r2 - r1) * i / height)
        g = int(g1 + (g2 - g1) * i / height)
        b = int(b1 + (b2 - b1) * i / height)
        
        color = f'#{r:04x}{g:04x}{b:04x}'
        
        canvas.create_line(0, i, width, i, fill=color, tags="gradient")

def on_resize(event):
    canvas_width = event.width
    canvas_height = event.height
    canvas.delete("gradient")
    create_gradient(canvas, canvas_width, canvas_height, "#8A2BE2", "#32CD32")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Jogo da Forca")
root.geometry("800x600")
root.resizable(True, True)  # Permite maximização

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)
create_gradient(canvas, 800, 600, "#8A2BE2", "#32CD32")

canvas.bind("<Configure>", on_resize)

frame = ttk.Frame(canvas, padding="10")
frame.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

# Configuração da fonte
font_style = ("Helvetica", 14, "bold")

label_palavra = ttk.Label(frame, text="", font=font_style)
label_palavra.pack(pady=5)

label_tentativas = ttk.Label(frame, text="Tentativas restantes: 6", font=font_style)
label_tentativas.pack(pady=5)

label_letra = ttk.Label(frame, text="Digite uma letra:", font=font_style)
label_letra.pack(pady=5)

entry_letra = ttk.Entry(frame, font=font_style)
entry_letra.pack(pady=5)

button_verificar = ttk.Button(frame, text="Verificar", command=verificar_letra)
button_verificar.pack(pady=5)

label_mensagem = ttk.Label(frame, text="", font=font_style)
label_mensagem.pack(pady=5)

button_iniciar = ttk.Button(frame, text="Iniciar Jogo", command=iniciar_jogo)
button_iniciar.pack(pady=5)

iniciar_jogo()

root.mainloop()