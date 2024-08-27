from tkinter import *

root = Tk()
root.title('Radio Buttons')

# r = IntVar()

MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text,variable=pizza,value=mode, command=lambda: selected(pizza.get())).pack(anchor=W)


def selected(value):
    my_label = Label(root, text=value)
    my_label.pack()


"""
Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: selected(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: selected(r.get())).pack()
"""

my_label = Label(root, text=pizza.get())
my_label.pack()


root.mainloop()