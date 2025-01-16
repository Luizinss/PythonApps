import tkinter as tk
from tkinter import ttk

def converter_unidades(valor, unidade_origem, unidade_destino):
    # Taxas de conversão para a unidade base (metros para distâncias, gramas para massas, mililitros para volumes)
    taxas_de_conversao_para_base = {
        "centímetros": 0.01,
        "metros": 1,
        "quilômetros": 1000,
        "miligramas": 0.001,
        "gramas": 1,
        "quilogramas": 1000,
        "mililitros": 1,
        "litros": 1000
    }
    
    # Converte o valor para a unidade base
    valor_em_unidade_base = valor * taxas_de_conversao_para_base[unidade_origem]
    
    # Converte da unidade base para a unidade de destino
    valor_convertido = valor_em_unidade_base / taxas_de_conversao_para_base[unidade_destino]
    
    return valor_convertido

def formatar_unidade(valor, unidade):
    if valor == 1:
        return f"{valor} {unidade[:-1]}" if unidade.endswith("s") else f"{valor} {unidade}"
    else:
        return f"{valor} {unidade}"

def converter():
    try:
        valor = float(entry_valor.get())
        unidade_origem = combo_origem.get()
        unidade_destino = combo_destino.get()
        resultado = converter_unidades(valor, unidade_origem, unidade_destino)
        valor_formatado = formatar_unidade(valor, unidade_origem)
        resultado_formatado = formatar_unidade(resultado, unidade_destino)
        label_resultado.config(text=f"{valor_formatado} = {resultado_formatado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira um valor numérico válido.")

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
root.title("Conversor de Unidades")
root.geometry("400x300")
root.resizable(False, False)  # Desabilita maximização

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill=tk.BOTH, expand=True)
create_gradient(canvas, 400, 300, "#FF0000", "#FF69B4")

frame = ttk.Frame(canvas, padding="10")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Configuração da fonte
font_style = ("Helvetica", 12, "bold")

label_valor = ttk.Label(frame, text="Valor:", font=font_style)
label_valor.grid(row=0, column=0, padx=5, pady=5)

entry_valor = ttk.Entry(frame, width=20, font=font_style)
entry_valor.grid(row=0, column=1, padx=5, pady=5)

label_origem = ttk.Label(frame, text="Unidade de Origem:", font=font_style)
label_origem.grid(row=1, column=0, padx=5, pady=5)

combo_origem = ttk.Combobox(frame, values=["centímetros", "metros", "quilômetros", "miligramas", "gramas", "quilogramas", "mililitros", "litros"], font=font_style)
combo_origem.grid(row=1, column=1, padx=5, pady=5)
combo_origem.current(0)

label_destino = ttk.Label(frame, text="Unidade de Destino:", font=font_style)
label_destino.grid(row=2, column=0, padx=5, pady=5)

combo_destino = ttk.Combobox(frame, values=["centímetros", "metros", "quilômetros", "miligramas", "gramas", "quilogramas", "mililitros", "litros"], font=font_style)
combo_destino.grid(row=2, column=1, padx=5, pady=5)
combo_destino.current(1)

button_converter = ttk.Button(frame, text="Converter", command=converter, style="TButton")
button_converter.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

label_resultado = ttk.Label(frame, text="", font=font_style)
label_resultado.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()