import tkinter as tk

# Function to update the expression in the entry widget
def press(num):
    current_expression = expression.get()
    expression.set(current_expression + str(num))

# Function to evaluate the final expression
def equalpress():
    try:
        total = str(eval(expression.get()))
        expression.set(total)
    except:
        expression.set("Error")

# Function to clear the entry widget
def clear():
    expression.set("")

# Creating the main window
root = tk.Tk()
root.title("Simple Calculator")

expression = tk.StringVar()

# Entry widget for displaying the expression
entry = tk.Entry(root, textvariable=expression, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Creating the buttons
button1 = tk.Button(root, text='1', padx=20, pady=20, command=lambda: press(1))
button2 = tk.Button(root, text='2', padx=20, pady=20, command=lambda: press(2))
button3 = tk.Button(root, text='3', padx=20, pady=20, command=lambda: press(3))
button4 = tk.Button(root, text='4', padx=20, pady=20, command=lambda: press(4))
button5 = tk.Button(root, text='5', padx=20, pady=20, command=lambda: press(5))
button6 = tk.Button(root, text='6', padx=20, pady=20, command=lambda: press(6))
button7 = tk.Button(root, text='7', padx=20, pady=20, command=lambda: press(7))
button8 = tk.Button(root, text='8', padx=20, pady=20, command=lambda: press(8))
button9 = tk.Button(root, text='9', padx=20, pady=20, command=lambda: press(9))
button0 = tk.Button(root, text='0', padx=19, pady=20, command=lambda: press(0))

plus = tk.Button(root, text='+', padx=18, pady=20, command=lambda: press("+"))
minus = tk.Button(root, text='-', padx=20, pady=20, command=lambda: press("-"))
multiply = tk.Button(root, text='*', padx=20, pady=20, command=lambda: press("*"))
divide = tk.Button(root, text='/', padx=20, pady=20, command=lambda: press("/"))

equal = tk.Button(root, text='=', padx=74, pady=20, command=equalpress)
clear_button = tk.Button(root, text='C', padx=74, pady=20, command=clear)

# Placing buttons on the grid
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
plus.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
minus.grid(row=2, column=3)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
multiply.grid(row=3, column=3)

clear_button.grid(row=4, column=0, columnspan=3)
button0.grid(row=4, column=3)


equal.grid(row=5, column=0, columnspan=3)
divide.grid(row=5, column=3)

# Running the main loop
root.mainloop()
