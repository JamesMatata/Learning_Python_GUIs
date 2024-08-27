from tkinter import *

root = Tk()
root.title('Check Box')
root.geometry('400x400')

def show():
    my_label = Label(root, text=selected.get()).pack()

days_list = [
    'Monday', 
    'Tuesday', 
    'Wednesday', 
    'Thursday', 
    'Friday'
    ]

selected = StringVar()
selected.set(days_list[0])


# drop = OptionMenu(root, selected, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
drop = OptionMenu(root, selected, *days_list)
drop.pack()

my_button = Button(root, text='Show selection', command=show).pack()

root.mainloop()