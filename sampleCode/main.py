import customtkinter as ctk
from tkinter import StringVar

app = ctk.CTk()
app.title("Calculator")
app.geometry("400x500")

expression = StringVar()
entry = ctk.CTkEntry(app, textvariable=expression, font=("Helvetica", 20), justify="right", width=350, height=50)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def press(key):
    current_expression = expression.get()
    expression.set(current_expression + str(key))

def clear():
    expression.set("")

def equal():
    try:
        result = str(eval(expression.get()))
        expression.set(result)
    except:
        expression.set("Error")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0
for button_text in buttons:
    if button_text == "=":
        button = ctk.CTkButton(app, text=button_text, command=equal, font=("Helvetica", 20), width=80, height=80)
    else:
        button = ctk.CTkButton(app, text=button_text, command=lambda bt=button_text: press(bt), font=("Helvetica", 20), width=80, height=80)
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

clear_button = ctk.CTkButton(app, text="C", command=clear, font=("Helvetica", 20), width=80, height=80)
clear_button.grid(row=row_val, column=col_val, columnspan=2, padx=5, pady=5, sticky="nsew")

app.mainloop()
