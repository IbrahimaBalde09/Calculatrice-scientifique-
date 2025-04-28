from tkinter import *
import math

# Fenêtre principale
calc = Tk()
calc.title("Calculatrice Scientifique")

operator = ""
text_input = StringVar()

# Fonctions des boutons
def btnClick(numbers):
    global operator
    operator += str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_input.set("")

def btnEquals():
    global operator
    try:
        result = str(eval(operator))
        text_input.set(result)
        operator = ""
    except:
        text_input.set("Erreur")
        operator = ""

def btnSqrt():
    global operator
    try:
        result = str(math.sqrt(eval(operator)))
        text_input.set(result)
        operator = ""
    except:
        text_input.set("Erreur")
        operator = ""

def btnSquare():
    global operator
    try:
        result = str(eval(operator) ** 2)
        text_input.set(result)
        operator = ""
    except:
        text_input.set("Erreur")
        operator = ""

def btnTrig(func):
    global operator
    try:
        val = eval(operator)
        if func == "sin":
            result = str(math.sin(math.radians(val)))
        elif func == "cos":
            result = str(math.cos(math.radians(val)))
        elif func == "tan":
            result = str(math.tan(math.radians(val)))
        text_input.set(result)
        operator = ""
    except:
        text_input.set("Erreur")
        operator = ""

def btnLog():
    global operator
    try:
        result = str(math.log10(eval(operator)))
        text_input.set(result)
        operator = ""
    except:
        text_input.set("Erreur")
        operator = ""

# Affichage
textDisplay = Entry(calc, font=('arial', 20, 'bold'), textvariable=text_input, bd=20, insertwidth=4, bg="#e6f2ff", justify='right')
textDisplay.grid(columnspan=5)

# Boutons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3), ('√', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3), ('x²', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3), ('log', 3, 4),
    ('0', 4, 0), ('Clr', 4, 1), ('=', 4, 2), ('/', 4, 3),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2)
]

for (text, row, col) in buttons:
    if text == 'Clr':
        action = btnClear
    elif text == '=':
        action = btnEquals
    elif text == '√':
        action = btnSqrt
    elif text == 'x²':
        action = btnSquare
    elif text == 'log':
        action = btnLog
    elif text in ['sin', 'cos', 'tan']:
        action = lambda x=text: btnTrig(x)
    else:
        action = lambda x=text: btnClick(x)

    Button(calc, text=text, padx=16, pady=16, bd=8, fg='white' if text in ['√', 'x²', 'log', 'sin', 'cos', 'tan'] else 'black',
           font=('arial', 18, 'bold'), bg="#4da6ff" if text in ['√', 'x²', 'log', 'sin', 'cos', 'tan'] else "#cce6ff", command=action)\
        .grid(row=row, column=col)

calc.mainloop()