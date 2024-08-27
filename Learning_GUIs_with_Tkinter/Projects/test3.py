import tkinter as tk
from tkinter import ttk
import math

# Function to calculate area
def calculate_area(shape):
    try:
        if shape == "Square":
            side = float(entry1.get())
            result = side ** 2
        elif shape == "Rectangle":
            length = float(entry1.get())
            width = float(entry2.get())
            result = length * width
        elif shape == "Circle":
            radius = float(entry1.get())
            result = math.pi * (radius ** 2)
        elif shape == "Triangle":
            base = float(entry1.get())
            height = float(entry2.get())
            result = 0.5 * base * height
        else:
            result = "Select a valid shape"
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Function to calculate volume
def calculate_volume(solid):
    try:
        if solid == "Cube":
            side = float(entry1.get())
            result = side ** 3
        elif solid == "Rectangular Prism":
            length = float(entry1.get())
            width = float(entry2.get())
            height = float(entry3.get())
            result = length * width * height
        elif solid == "Sphere":
            radius = float(entry1.get())
            result = (4/3) * math.pi * (radius ** 3)
        elif solid == "Cylinder":
            radius = float(entry1.get())
            height = float(entry2.get())
            result = math.pi * (radius ** 2) * height
        else:
            result = "Select a valid solid"
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Function to update input fields
def update_inputs(option, choice):
    for widget in input_frame.winfo_children():
        widget.destroy()

    if choice == "Area":
        if option in ["Square", "Circle"]:
            tk.Label(input_frame, text=f"Enter {option} dimension:").grid(row=0, column=0)
            global entry1
            entry1 = tk.Entry(input_frame)
            entry1.grid(row=0, column=1)
        elif option in ["Rectangle", "Triangle"]:
            tk.Label(input_frame, text="Enter length/base:").grid(row=0, column=0)
            entry1 = tk.Entry(input_frame)
            entry1.grid(row=0, column=1)

            tk.Label(input_frame, text="Enter width/height:").grid(row=1, column=0)
            global entry2
            entry2 = tk.Entry(input_frame)
            entry2.grid(row=1, column=1)
        
        calculate_button.config(command=lambda: calculate_area(option))

    elif choice == "Volume":
        if option == "Cube":
            tk.Label(input_frame, text=f"Enter {option} side:").grid(row=0, column=0)
            entry1 = tk.Entry(input_frame)
            entry1.grid(row=0, column=1)
        elif option == "Rectangular Prism":
            tk.Label(input_frame, text="Enter length:").grid(row=0, column=0)
            entry1 = tk.Entry(input_frame)
            entry1.grid(row=0, column=1)

            tk.Label(input_frame, text="Enter width:").grid(row=1, column=0)
            entry2 = tk.Entry(input_frame)
            entry2.grid(row=1, column=1)

            tk.Label(input_frame, text="Enter height:").grid(row=2, column=0)
            global entry3
            entry3 = tk.Entry(input_frame)
            entry3.grid(row=2, column=1)
        elif option in ["Sphere", "Cylinder"]:
            tk.Label(input_frame, text="Enter radius:").grid(row=0, column=0)
            entry1 = tk.Entry(input_frame)
            entry1.grid(row=0, column=1)

            if option == "Cylinder":
                tk.Label(input_frame, text="Enter height:").grid(row=1, column=0)
                entry2 = tk.Entry(input_frame)
                entry2.grid(row=1, column=1)
        
        calculate_button.config(command=lambda: calculate_volume(option))

# Function to show appropriate options based on area/volume choice
def show_options(choice):
    if choice == "Area":
        options = ["Square", "Rectangle", "Circle", "Triangle"]
    else:
        options = ["Cube", "Rectangular Prism", "Sphere", "Cylinder"]

    shape_var.set(options[0])
    option_menu = ttk.OptionMenu(option_frame, shape_var, options[0], *options)
    option_menu.grid(row=0, column=1)
    update_inputs(options[0], choice)

# Main window setup
root = tk.Tk()
root.title("Area and Volume Calculator")
root.geometry("400x300")

# Frame for choosing Area or Volume
choice_frame = tk.Frame(root)
choice_frame.pack(pady=10)

tk.Label(choice_frame, text="Choose Calculation:").grid(row=0, column=0)

choice_var = tk.StringVar()
choice_var.set("Area")

choice_menu = ttk.OptionMenu(choice_frame, choice_var, "Area", "Area", "Volume", command=show_options)
choice_menu.grid(row=0, column=1)

# Frame for choosing specific shape or solid
option_frame = tk.Frame(root)
option_frame.pack(pady=10)

tk.Label(option_frame, text="Choose Shape/Solid:").grid(row=0, column=0)

shape_var = tk.StringVar()
shape_var.set("Square")

# Initial option menu (default: Area -> Square)
option_menu = ttk.OptionMenu(option_frame, shape_var, "Square", "Square", "Rectangle", "Circle", "Triangle", command=lambda _: update_inputs(shape_var.get(), choice_var.get()))
option_menu.grid(row=0, column=1)

# Frame for input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Result:", font=("Helvetica", 14))
result_label.pack(pady=20)

# Calculate button
calculate_button = ttk.Button(root, text="Calculate")
calculate_button.pack()

# Show initial inputs (default: Area -> Square)
update_inputs("Square", "Area")

root.mainloop()
