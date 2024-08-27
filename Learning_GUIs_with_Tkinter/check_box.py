from tkinter import *

root = Tk()
root.title('Check Box')
root.geometry('400x400')

def show():
    my_label = Label(root, text=var.get()).pack()

# var = IntVar()
var = StringVar()

c = Checkbutton(root, text='Check me!', variable=var, onvalue='On', offvalue='Off')
c.deselect()
c.pack()

my_button = Button(root, text='Show Selection', command=show)
my_button.pack()

root.mainloop()