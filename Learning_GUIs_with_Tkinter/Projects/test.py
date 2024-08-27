from tkinter import *
from PIL import ImageTk, Image

# Must install pillow

root = Tk()
root.title('Images')
# root.iconbitmap('icon.ico')

# Desired size for the container
container_width = 300
container_height = 400

# Open, resize, and convert images to PhotoImage format while maintaining aspect ratio
def open_image(filepath, container_width, container_height):
    img = Image.open(filepath)
    
    # Calculate the appropriate size with aspect ratio maintained
    img_ratio = img.width / img.height
    container_ratio = container_width / container_height
    
    if img_ratio > container_ratio:
        new_width = container_width
        new_height = int(container_width / img_ratio)
    else:
        new_width = int(container_height * img_ratio)
        new_height = container_height
    
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

my_img1 = open_image("files/image1.jpeg", container_width, container_height)
my_img2 = open_image("files/image2.jpg", container_width, container_height)
my_img3 = open_image("files/image3.JPG", container_width, container_height)
my_img4 = open_image("files/image4.jpg", container_width, container_height)
my_img5 = open_image("files/image5.jpg", container_width, container_height)

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text=f'Image 1 of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global forward_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    back_button = Button(root, text='<<', command=lambda: back(image_number-1))
    status = Label(root, text=f'Image {image_number} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)

    if image_number == len(image_list):
        forward_button = Button(root, text='>>', state=DISABLED)
    else:
        forward_button = Button(root, text='>>', command=lambda: forward(image_number+1))

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0, sticky=W+E)
    exit_button.grid(row=1, column=1, sticky=W+E)
    forward_button.grid(row=1, column=2, pady=10, sticky=W+E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global forward_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    forward_button = Button(root, text='>>', command=lambda: forward(image_number+1))
    status = Label(root, text=f'Image {image_number} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)

    if image_number == 1:
        back_button = Button(root, text='<<', state=DISABLED)
    else:
        back_button = Button(root, text='<<', command=lambda: back(image_number-1))

    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0, sticky=W+E)
    exit_button.grid(row=1, column=1, sticky=W+E)
    forward_button.grid(row=1, column=2, pady=10, sticky=W+E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

back_button = Button(root, text='<<', state=DISABLED)
exit_button = Button(root, text='Exit', command=root.quit)
forward_button = Button(root, text='>>', command=lambda: forward(2))

back_button.grid(row=1, column=0, sticky=W+E)
exit_button.grid(row=1, column=1, sticky=W+E)
forward_button.grid(row=1, column=2, pady=10, sticky=W+E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
