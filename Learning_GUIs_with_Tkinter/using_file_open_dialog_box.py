from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# main window
root = Tk()
root.title('Using file open dialog Box')

def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="/", title='Select a file', filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_label2 = Label(image=my_img)
    my_label2.pack()

my_button = Button(root, text='Open file', command=open).pack()

root.mainloop()