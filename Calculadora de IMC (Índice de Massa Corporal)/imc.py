import tkinter as tk
from tkinter import ttk

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.99:
        return "Peso normal"
    elif 25 <= imc < 29.99:
        return "Sobrepeso"
    else:
        return "Obesidade"

def calcular():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        label_resultado.config(text=f"IMC: {imc:.2f} - {classificacao}")
    except ValueError:
        label_resultado.config(text="Por favor, insira valores numéricos válidos.")

def create_gradient(canvas, width, height, color1, color2):
    for i in range(height):
        r1, g1, b1 = canvas.winfo_rgb(color1)
        r2, g2, b2 = canvas.winfo_rgb(color2)
        
        r = int(r1 + (r2 - r1) * i / height)
        g = int(g1 + (g2 - g1) * i / height)
        b = int(b1 + (b2 - b1) * i / height)
        
        color = f'#{r:04x}{g:04x}{b:04x}'
        
        canvas.create_line(0, i, width, i, fill=color)

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("400x300")
root.resizable(False, False)  # Desabilita maximização

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill=tk.BOTH, expand=True)
create_gradient(canvas, 400, 300, "#FF5733", "#C70039")

frame = ttk.Frame(canvas, padding="10")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Configuração da fonte
font_style = ("Helvetica", 12, "bold")

# Criação de widgets com bordas arredondadas
create_rounded_rectangle(canvas, 50, 50, 350, 250, radius=20, fill="white", outline="")

label_peso = ttk.Label(frame, text="Peso (kg):", font=font_style)
label_peso.grid(row=0, column=0, padx=5, pady=5)

entry_peso = ttk.Entry(frame, width=20, font=font_style)
entry_peso.grid(row=0, column=1, padx=5, pady=5)

label_altura = ttk.Label(frame, text="Altura (m):", font=font_style)
label_altura.grid(row=1, column=0, padx=5, pady=5)

entry_altura = ttk.Entry(frame, width=20, font=font_style)
entry_altura.grid(row=1, column=1, padx=5, pady=5)

button_calcular = ttk.Button(frame, text="Calcular", command=calcular)
button_calcular.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

label_resultado = ttk.Label(frame, text="", font=font_style)
label_resultado.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()