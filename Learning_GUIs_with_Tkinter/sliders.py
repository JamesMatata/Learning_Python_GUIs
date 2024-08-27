from tkinter import *

root = Tk()
root.title('Sliders')

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200,orient=HORIZONTAL)
horizontal.pack()

def slide():
    Label(root, text=horizontal.get()).pack()

btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()