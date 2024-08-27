from tkinter import *
from PIL import ImageTk, Image

# Must install pillow

root = Tk()
root.title('Images')
# root.iconbitmap('icon.ico')

my_img = ImageTk.PhotoImage(Image.open("files/image.jpeg"))
my_label = Label(image=my_img)
my_label.pack()


root.mainloop()