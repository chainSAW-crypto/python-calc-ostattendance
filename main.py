import tkinter as tk
from tkinter import messagebox
import math

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

def scientific_operation(op):
    try:
        value = float(entry_var.get())
        if op == "sin":
            result = math.sin(math.radians(value))
        elif op == "cos":
            result = math.cos(math.radians(value))
        elif op == "tan":
            result = math.tan(math.radians(value))
        elif op == "log":
            result = math.log10(value)
        elif op == "ln":
            result = math.log(value)
        elif op == "sqrt":
            result = math.sqrt(value)
        entry_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Operation")

root = tk.Tk()
root.title("Scientific Calculator")
entry_var = tk.StringVar()

tk.Entry(root, textvariable=entry_var, font="Arial 20", justify="right").grid(row=0, column=0, columnspan=6)

buttons = [
    ("7", "8", "9", "/", "sin", "cos"),
    ("4", "5", "6", "*", "tan", "log"),
    ("1", "2", "3", "-", "ln", "sqrt"),
    ("C", "0", "=", "+")
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        btn = tk.Button(root, text=text, font="Arial 15", padx=20, pady=20)
        btn.grid(row=i+1, column=j)
        if text in "0123456789+-*/=C":
            btn.bind("<Button-1>", on_click)
        else:
            btn.config(command=lambda t=text: scientific_operation(t))

root.mainloop()
