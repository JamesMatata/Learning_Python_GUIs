from tkinter import *

root = Tk()

e = Entry(root, width=50, fg= 'white', bg='blue', borderwidth=5)
e.pack()
e.insert(0, "Enter your name: ")

def my_click():
    text_input = e.get()
    my_label = Label(root, text=text_input)
    my_label.pack()

my_button = Button(root, text='Enter your Name', padx=20, pady=10, command=my_click, fg='red', bg='blue')
my_button.pack()


root.mainloop()