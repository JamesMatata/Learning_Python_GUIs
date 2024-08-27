from tkinter import *

root = Tk()

my_label1 = Label(root, text="Hello Tkinter!")
my_label2 = Label(root, text="Python Programming")

my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=0)

root.mainloop()