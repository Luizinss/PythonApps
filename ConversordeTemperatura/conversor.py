import tkinter as tk
from tkinter import ttk, messagebox

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        conversion_type = combo_conversion.get()
        
        if conversion_type == "Celsius para Fahrenheit":
            result = celsius_to_fahrenheit(temp)
            unit = "°F"
        elif conversion_type == "Fahrenheit para Celsius":
            result = fahrenheit_to_celsius(temp)
            unit = "°C"
        elif conversion_type == "Celsius para Kelvin":
            result = celsius_to_kelvin(temp)
            unit = "K"
        elif conversion_type == "Kelvin para Celsius":
            result = kelvin_to_celsius(temp)
            unit = "°C"
        elif conversion_type == "Fahrenheit para Kelvin":
            result = fahrenheit_to_kelvin(temp)
            unit = "K"
        elif conversion_type == "Kelvin para Fahrenheit":
            result = kelvin_to_fahrenheit(temp)
            unit = "°F"
        else:
            messagebox.showerror("Erro", "Selecione um tipo de conversão válido.")
            return
        
        label_result.config(text=f"Resultado: {result:.2f} {unit}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

def create_gradient(canvas, width, height, color1, color2, color3):
    for i in range(height):
        r1, g1, b1 = canvas.winfo_rgb(color1)
        r2, g2, b2 = canvas.winfo_rgb(color2)
        r3, g3, b3 = canvas.winfo_rgb(color3)
        
        r = int(r1 + (r2 - r1) * i / height)
        g = int(g1 + (g2 - g1) * i / height)
        b = int(b1 + (b2 - b1) * i / height)
        
        color = f'#{r:04x}{g:04x}{b:04x}'
        
        canvas.create_line(0, i, width, i, fill=color)
        
        r = int(r2 + (r3 - r2) * i / height)
        g = int(g2 + (g3 - g2) * i / height)
        b = int(b2 + (b3 - b2) * i / height)
        
        color = f'#{r:04x}{g:04x}{b:04x}'
        
        canvas.create_line(0, i, width, i, fill=color)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Conversor de Temperaturas")

canvas = tk.Canvas(root, width=400, height=300)
canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
create_gradient(canvas, 400, 300, "#ADD8E6", "#90EE90", "#D8BFD8")

frame = ttk.Frame(canvas, padding="10")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label_temp = ttk.Label(frame, text="Temperatura:")
label_temp.grid(row=0, column=0, padx=5, pady=5)

entry_temp = ttk.Entry(frame)
entry_temp.grid(row=0, column=1, padx=5, pady=5)

label_conversion = ttk.Label(frame, text="Conversão:")
label_conversion.grid(row=1, column=0, padx=5, pady=5)

combo_conversion = ttk.Combobox(frame, values=[
    "Celsius para Fahrenheit",
    "Fahrenheit para Celsius",
    "Celsius para Kelvin",
    "Kelvin para Celsius",
    "Fahrenheit para Kelvin",
    "Kelvin para Fahrenheit"
])
combo_conversion.grid(row=1, column=1, padx=5, pady=5)
combo_conversion.current(0)

button_convert = ttk.Button(frame, text="Converter", command=convert_temperature)
button_convert.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

label_result = ttk.Label(frame, text="Resultado:")
label_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()