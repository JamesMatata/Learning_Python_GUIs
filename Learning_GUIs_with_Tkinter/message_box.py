from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Message Boxes')

# Types of messageboxes: showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def info():
    messagebox.showinfo("This is my popup title!","This is the actuall content of the popup box")

def warning():
    messagebox.showwarning("This is my popup title!","This is the actuall content of the popup box")

def error():
    messagebox.showerror("This is my popup title!","This is the actuall content of the popup box")

def question():
    response=messagebox.askquestion("This is my popup title!","This is the actuall content of the popup box")
    print(response)

def okcancel():
    response=messagebox.askokcancel("This is my popup title!","This is the actuall content of the popup box")
    print(response)

def yesno():
    response=messagebox.askyesno("This is my popup title!","This is the actuall content of the popup box")
    print(response)

Button(root, text='Info Messagebox', command=info).pack(padx=10,pady=10)
Button(root, text='Warning Messagebox', command=warning).pack(padx=10,pady=10)
Button(root, text='Error Messagebox', command=error).pack(padx=10,pady=10)
Button(root, text='Question Messagebox', command=question).pack(padx=10,pady=10)
Button(root, text='OkCancel Messagebox', command=okcancel).pack(padx=10,pady=10)
Button(root, text='YesNo Messagebox', command=yesno).pack(padx=10,pady=10)

root.mainloop()