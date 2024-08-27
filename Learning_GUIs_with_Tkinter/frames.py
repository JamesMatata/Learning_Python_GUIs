from tkinter import *

root = Tk()
root.title('Frames')

frame = LabelFrame(root, padx=50, pady=5)
frame.pack(padx=10,pady=10)

b1 = Button(frame, text='Button1')
b2 = Button(frame, text='Button2')

b1.grid(row=0,column=0,pady=5)
b2.grid(row=1,column=0,pady=5)

root.mainloop()