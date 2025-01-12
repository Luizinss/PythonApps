import tkinter as tk
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")
    current_text = screen_var.get()
    
    if text == "=":
        try:
            result = str(eval(current_text.replace('x', '*')))
            screen_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            screen_var.set("")
    elif text == "C":
        screen_var.set("")
    else:
        if text in "+-*/x":
            if current_text == "" or current_text[-1] in "+-*/x":
                return
        screen_var.set(current_text + text)

root = tk.Tk()
root.title("Calculadora")
root.configure(bg="lightblue")
root.resizable(False, False)

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack()

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', 'x',  # Trocando * por x
    'C', '0', '=', '/',
    '.',  # Adicionando o botão de ponto decimal
]

i = 0
for btn in buttons:
    button = tk.Button(button_frame, text=btn, font="lucida 15 bold", bg="lightgray", fg="black", relief="raised", bd=5)
    button.grid(row=i//4, column=i%4, padx=10, pady=10)
    button.bind("<Button-1>", click)
    i += 1

root.mainloop()