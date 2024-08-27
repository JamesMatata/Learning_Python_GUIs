from tkinter import *

# main window
root = Tk()
root.title('Creating new Windows')
def open():
    # window 2
    top = Toplevel()
    Button(top, text='Close Window', command=top.destroy).pack()

Button(root, text='Open second window', command=open).pack()


root.mainloop()