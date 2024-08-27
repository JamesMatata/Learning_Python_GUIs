from tkinter import *

root = Tk()

def my_click():
    my_label = Label(root, text='The button was clicked!')
    my_label.pack()


my_button = Button(root, text='Click Me', padx=50, pady=10, command=my_click, fg='red', bg='blue')
my_button.pack()


root.mainloop()