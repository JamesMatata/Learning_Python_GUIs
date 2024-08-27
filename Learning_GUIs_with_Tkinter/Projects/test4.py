import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime

# Initialize the database
conn = sqlite3.connect('library.db')
c = conn.cursor()

# Create tables if they don't exist
c.execute('''CREATE TABLE IF NOT EXISTS students (
             id INTEGER PRIMARY KEY, 
             name TEXT, 
             student_id TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS books (
             id INTEGER PRIMARY KEY, 
             title TEXT, 
             author TEXT, 
             isbn TEXT, 
             genre TEXT, 
             available INTEGER)''')

c.execute('''CREATE TABLE IF NOT EXISTS transactions (
             id INTEGER PRIMARY KEY, 
             student_name TEXT, 
             student_id TEXT, 
             book_id INTEGER, 
             borrow_date TEXT, 
             due_date TEXT, 
             return_date TEXT,
             returned INTEGER)''')

conn.commit()

# Functions for book management (Admin only)
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    genre = genre_entry.get()

    if title and author and isbn and genre:
        c.execute("INSERT INTO books (title, author, isbn, genre, available) VALUES (?, ?, ?, ?, 1)",
                  (title, author, isbn, genre))
        conn.commit()
        messagebox.showinfo("Success", "Book added successfully!")
        clear_book_entries()
        refresh_books()
    else:
        messagebox.showerror("Error", "All fields are required!")

def clear_book_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)
    genre_entry.delete(0, tk.END)

def refresh_books():
    for row in book_tree.get_children():
        book_tree.delete(row)
    
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    for book in books:
        book_tree.insert('', tk.END, values=book)

def borrow_book():
    student_name = student_name_entry.get()
    student_id = student_id_entry.get()
    selected_item = book_tree.selection()
    if selected_item and student_name and student_id:
        book_id = book_tree.item(selected_item)['values'][0]
        borrow_date = datetime.now().strftime('%Y-%m-%d')
        due_date = due_date_entry.get()
        
        c.execute("INSERT INTO transactions (student_name, student_id, book_id, borrow_date, due_date, returned) VALUES (?, ?, ?, ?, ?, 0)",
                  (student_name, student_id, book_id, borrow_date, due_date))
        c.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
        conn.commit()
        messagebox.showinfo("Success", "Book borrowed successfully!")
        clear_borrow_entries()
        refresh_books()
    else:
        messagebox.showerror("Error", "All fields are required and a book must be selected!")

def clear_borrow_entries():
    student_name_entry.delete(0, tk.END)
    student_id_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)

def mark_returned():
    selected_item = transaction_tree.selection()
    if selected_item:
        transaction_id = transaction_tree.item(selected_item)['values'][0]
        return_date = datetime.now().strftime('%Y-%m-%d')
        
        c.execute("UPDATE transactions SET return_date=?, returned=1 WHERE id=?", (return_date, transaction_id))
        book_id = transaction_tree.item(selected_item)['values'][3]
        c.execute("UPDATE books SET available=1 WHERE id=?", (book_id,))
        conn.commit()
        messagebox.showinfo("Success", "Book marked as returned!")
        refresh_transactions()
    else:
        messagebox.showerror("Error", "No transaction selected!")

def refresh_transactions():
    for row in transaction_tree.get_children():
        transaction_tree.delete(row)
    
    c.execute("SELECT * FROM transactions")
    transactions = c.fetchall()
    for transaction in transactions:
        transaction_tree.insert('', tk.END, values=transaction)

# Separate windows for books and borrowed books
def open_books_window():
    books_window = tk.Toplevel(admin_dashboard_window)
    books_window.title("Manage Books - Library Management System")

    global book_tree, title_entry, author_entry, isbn_entry, genre_entry

    # Book management section
    book_frame = tk.Frame(books_window)
    book_frame.pack(pady=20)

    book_tree = ttk.Treeview(book_frame, columns=('ID', 'Title', 'Author', 'ISBN', 'Genre', 'Available'), show='headings')
    book_tree.heading('ID', text='ID')
    book_tree.heading('Title', text='Title')
    book_tree.heading('Author', text='Author')
    book_tree.heading('ISBN', text='ISBN')
    book_tree.heading('Genre', text='Genre')
    book_tree.heading('Available', text='Available')
    book_tree.pack()
    refresh_books()
    
    form_frame = tk.Frame(books_window)
    form_frame.pack(pady=20)

    tk.Label(form_frame, text="Title:").grid(row=0, column=0, padx=10, pady=5)
    title_entry = tk.Entry(form_frame)
    title_entry.grid(row=0, column=1, pady=5)

    tk.Label(form_frame, text="Author:").grid(row=1, column=0, padx=10, pady=5)
    author_entry = tk.Entry(form_frame)
    author_entry.grid(row=1, column=1, pady=5)

    tk.Label(form_frame, text="ISBN:").grid(row=2, column=0, padx=10, pady=5)
    isbn_entry = tk.Entry(form_frame)
    isbn_entry.grid(row=2, column=1, pady=5)

    tk.Label(form_frame, text="Genre:").grid(row=3, column=0, padx=10, pady=5)
    genre_entry = tk.Entry(form_frame)
    genre_entry.grid(row=3, column=1, pady=5)

    add_book_button = tk.Button(form_frame, text="Add Book", command=add_book)
    add_book_button.grid(row=4, columnspan=2, pady=10)

def open_borrowed_books_window():
    borrowed_books_window = tk.Toplevel(admin_dashboard_window)
    borrowed_books_window.title("Borrowed Books - Library Management System")

    global transaction_tree

    transaction_frame = tk.Frame(borrowed_books_window)
    transaction_frame.pack(pady=20)

    transaction_tree = ttk.Treeview(transaction_frame, columns=('ID', 'Student Name', 'Student ID', 'Book ID', 'Borrow Date', 'Due Date', 'Return Date', 'Returned'), show='headings')
    transaction_tree.heading('ID', text='ID')
    transaction_tree.heading('Student Name', text='Student Name')
    transaction_tree.heading('Student ID', text='Student ID')
    transaction_tree.heading('Book ID', text='Book ID')
    transaction_tree.heading('Borrow Date', text='Borrow Date')
    transaction_tree.heading('Due Date', text='Due Date')
    transaction_tree.heading('Return Date', text='Return Date')
    transaction_tree.heading('Returned', text='Returned')
    transaction_tree.pack()
    refresh_transactions()

    return_button = tk.Button(transaction_frame, text="Mark as Returned", command=mark_returned)
    return_button.pack(pady=10)

# Functions for user management (Admin only)
def register_student():
    name = reg_name_entry.get()
    student_id = reg_id_entry.get()

    if name and student_id:
        c.execute("INSERT INTO students (name, student_id) VALUES (?, ?)", (name, student_id))
        conn.commit()
        messagebox.showinfo("Success", "Student registered successfully!")
        clear_register_entries()
    else:
        messagebox.showerror("Error", "All fields are required!")

def clear_register_entries():
    reg_name_entry.delete(0, tk.END)
    reg_id_entry.delete(0, tk.END)

def logout():
    admin_dashboard_window.destroy()
    login_window()

# Admin Dashboard Home Page
def admin_dashboard():
    global admin_dashboard_window
    admin_dashboard_window = tk.Tk()
    admin_dashboard_window.title("Admin Dashboard - Library Management System")

    # Buttons for different functionalities
    books_button = tk.Button(admin_dashboard_window, text="Manage Books", command=open_books_window)
    books_button.pack(pady=10)

    borrowed_books_button = tk.Button(admin_dashboard_window, text="Borrowed Books", command=open_borrowed_books_window)
    borrowed_books_button.pack(pady=10)

    register_button = tk.Button(admin_dashboard_window, text="Register Student", command=register_window)
    register_button.pack(pady=10)

    logout_button = tk.Button(admin_dashboard_window, text="Logout", command=logout)
    logout_button.pack(pady=10)

    admin_dashboard_window.mainloop()

def register_window():
    global reg_name_entry, reg_id_entry
    reg_window = tk.Toplevel(admin_dashboard_window)
    reg_window.title("Register Student - Library Management System")

    tk.Label(reg_window, text="Student Name:").grid(row=0, column=0, padx=10, pady=5)
    reg_name_entry = tk.Entry(reg_window)
    reg_name_entry.grid(row=0, column=1, pady=5)

    tk.Label(reg_window, text="Student ID:").grid(row=1, column=0, padx=10, pady=5)
    reg_id_entry = tk.Entry(reg_window)
    reg_id_entry.grid(row=1, column=1, pady=5)

    register_button = tk.Button(reg_window, text="Register", command=register_student)
    register_button.grid(row=2, columnspan=2, pady=10)

# Login Window
def login_window():
    global login_username_entry, login_password_entry
    login_win = tk.Tk()
    login_win.title("Login - Library Management System")

    tk.Label(login_win, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    login_username_entry = tk.Entry(login_win)
    login_username_entry.grid(row=0, column=1, pady=5)

    tk.Label(login_win, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    login_password_entry = tk.Entry(login_win, show="*")
    login_password_entry.grid(row=1, column=1, pady=5)

    login_button = tk.Button(login_win, text="Login", command=lambda: [login_win.destroy(), admin_dashboard()])
    login_button.grid(row=2, columnspan=2, pady=10)

    login_win.mainloop()

# Start the application with the login window
login_window()

# Close the database connection when done
conn.close()
