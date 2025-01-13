import tkinter as tk
from tkinter import ttk
import requests

def obter_taxa_de_cambio(moeda_origem, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"
    response = requests.get(url)
    dados = response.json()
    return dados['rates'][moeda_destino]

def converter_moeda():
    try:
        valor = float(entry_valor.get())
        moeda_origem = combo_origem.get().split(" - ")[0]
        moeda_destino = combo_destino.get().split(" - ")[0]
        taxa = obter_taxa_de_cambio(moeda_origem, moeda_destino)
        valor_convertido = valor * taxa
        label_result.config(text=f"{valor} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}")
    except ValueError:
        label_result.config(text="Por favor, insira um valor numérico válido.")
    except Exception as e:
        label_result.config(text=f"Erro: {e}")

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
root.title("Conversor de Moeda")
root.resizable(False, False)  # Desabilita maximização

canvas = tk.Canvas(root, width=400, height=300)
canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
create_gradient(canvas, 400, 300, "#FF5733", "#C70039")

frame = ttk.Frame(canvas, padding="10")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Configuração da fonte
font_style = ("Helvetica", 12, "bold")

# Criando um estilo para o botão
style = ttk.Style()
style.configure("TButton", font=font_style)

label_valor = ttk.Label(frame, text="Valor:", font=font_style)
label_valor.grid(row=0, column=0, padx=5, pady=5)

entry_valor = ttk.Entry(frame, width=20, font=font_style)
entry_valor.grid(row=0, column=1, padx=5, pady=5)

label_origem = ttk.Label(frame, text="Moeda de Origem:", font=font_style)
label_origem.grid(row=1, column=0, padx=5, pady=5)

combo_origem = ttk.Combobox(frame, values=[
    "USD - Estados Unidos",
    "EUR - União Europeia",
    "BRL - Brasil",
    "JPY - Japão",
    "GBP - Reino Unido"
], font=font_style)
combo_origem.grid(row=1, column=1, padx=5, pady=5)
combo_origem.current(0)

label_destino = ttk.Label(frame, text="Moeda de Destino:", font=font_style)
label_destino.grid(row=2, column=0, padx=5, pady=5)

combo_destino = ttk.Combobox(frame, values=[
    "USD - Estados Unidos",
    "EUR - União Europeia",
    "BRL - Brasil",
    "JPY - Japão",
    "GBP - Reino Unido"
], font=font_style)
combo_destino.grid(row=2, column=1, padx=5, pady=5)
combo_destino.current(1)

button_converter = ttk.Button(frame, text="Converter", command=converter_moeda, style="TButton")
button_converter.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

label_result = ttk.Label(frame, text="", font=font_style)
label_result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()