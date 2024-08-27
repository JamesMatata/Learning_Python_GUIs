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
            student_id TEXT,
            school TEXT
            borrowed_books INTEGER)
          ''')

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
    title = title_entry_book_add.get()
    author = author_entry_book_add.get()
    isbn = isbn_entry_book_add.get()
    genre = genre_entry_book_add.get()

    if title and author and isbn and genre:
        c.execute("INSERT INTO books (title, author, isbn, genre, available) VALUES (?, ?, ?, ?, 1)",
                  (title, author, isbn, genre))
        conn.commit()
        messagebox.showinfo("Success", "Book added successfully!")
        cancel_book_add()
        refresh_books()

def refresh_books():
    for row in book_tree.get_children():
        book_tree.delete(row)
    
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    for book in books:
        book_tree.insert('', tk.END, values=book)

def clear_book_entries():
    title_entry_book_add.delete(0, tk.END)
    author_entry_book_add.delete(0, tk.END)
    isbn_entry_book_add.delete(0, tk.END)
    genre_entry_book_add.delete(0, tk.END)


def cancel_book_add():
    clear_book_entries()
    show_frame(all_books_frame)


def borrow_book():
    student_name = student_name_entry_book_borrow.get()
    student_id = student_id_entry_book_borrow.get()
    due_date = return_date_entry_book_borrow.get()
    selected_item = book_tree.selection()

    if selected_item and student_name and student_id and due_date:
        book_id = book_tree.item(selected_item)['values'][0]
        borrow_date = datetime.now().strftime('%Y-%m-%d')
        c.execute("INSERT INTO transactions (student_name, student_id, book_id, borrow_date, due_date, returned) VALUES (?, ?, ?, ?, ?, 0)",
                  (student_name, student_id, book_id, borrow_date, due_date))
        c.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
        conn.commit()
        messagebox.showinfo("Success", "Book borrowed successfully!")
        cancel_book_borrow()
        refresh_transactions()
    else:
        messagebox.showerror("Error", "All fields are required and a book must be selected!")

def clear_borrow_entries():
    student_name_entry_book_borrow.delete(0, tk.END)
    student_id_entry_book_borrow.delete(0, tk.END)
    return_date_entry_book_borrow.delete(0, tk.END)


def cancel_book_borrow():
    clear_borrow_entries()
    show_frame(all_books_frame)

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



# Main function
def show_frame(frame):
    """Function to switch frames"""
    frame.tkraise()

# Main window setup
root = tk.Tk()
root.title("Library Management System")

# Create frames (pages)
home_frame = tk.Frame(root)
all_books_frame = tk.Frame(root)
borrowed_books_frame = tk.Frame(root)
students_frame = tk.Frame(root)
add_book_frame = tk.Frame(root)
borrow_book_frame = tk.Frame(root)

for frame in (home_frame, all_books_frame, borrowed_books_frame, students_frame, add_book_frame,borrow_book_frame):
    frame.grid(row=0, column=0, sticky='nsew')

# Home Page
library_name = tk.Label(home_frame, text="lastKing Library\n", font=("Arial", 18))
library_name.grid(row=0,column=0, pady=5, ipadx=20)

manage_books_button = tk.Button(home_frame, text="Manage Books", command=lambda: show_frame(all_books_frame), padx=20, pady=5, bg='blue',fg='white')
manage_books_button.grid(row=1,column=0, pady=5, ipadx=20)

borrowed_books_button = tk.Button(home_frame, text="Borrowed Books", command=lambda: show_frame(borrowed_books_frame), padx=20, pady=5, bg='blue',fg='white')
borrowed_books_button.grid(row=2,column=0, pady=5, ipadx=16)

view_students_button = tk.Button(home_frame, text="View Students", command=lambda: show_frame(students_frame), padx=20, pady=5, bg='blue',fg='white')
view_students_button.grid(row=3,column=0, pady=5, ipadx=21)

# All books page -------------------------------------------------------------------------------------------------------------------------------------------------------
home_page_buton = tk.Button(all_books_frame, text="<<< Home Page", command=lambda: show_frame(home_frame), padx=20, pady=5, bg='blue',fg='white')
home_page_buton.grid(row=0,column=0)

label2 = tk.Label(all_books_frame, text="Manage Books", font=("Arial", 18))
label2.grid(row=0,column=6,columnspan=2)

add_book_buton = tk.Button(all_books_frame, text="Add book +", padx=25, pady=5, bg='blue',fg='white', anchor='w', command=lambda: show_frame(add_book_frame))
add_book_buton.grid(row=0,column=8)

borrow_book_buton = tk.Button(all_books_frame, text="Borrow Book", padx=25, pady=5, bg='blue',fg='white', anchor='w', command=lambda: show_frame(borrow_book_frame))
borrow_book_buton.grid(row=0,column=9)

book_tree = ttk.Treeview(all_books_frame, columns=('ID', 'Title', 'Author', 'ISBN', 'Genre', 'Available'), show='headings')
book_tree.heading('ID', text='ID')
book_tree.heading('Title', text='Title')
book_tree.heading('Author', text='Author')
book_tree.heading('ISBN', text='ISBN')
book_tree.heading('Genre', text='Genre')
book_tree.heading('Available', text='Available')
book_tree.grid(row=1,column=0,columnspan=10,padx=5, pady=5)
refresh_books()

# Add Book Page ---------------------------------------------------------------------------------------------------------------------------------------------------------
title_book_add = tk.Label(add_book_frame,text='Fill the form Below')
title_book_add.grid(row=0,column=0,columnspan=2,padx=40,pady=5)

title_label_book_add = tk.Label(add_book_frame,text='Book Title',anchor='w')
title_label_book_add.grid(row=1,column=0)
author_label_book_add = tk.Label(add_book_frame,text='Book Author',anchor='w')
author_label_book_add.grid(row=2,column=0)
isbn_label_book_add = tk.Label(add_book_frame,text='Book ISBN',anchor='w')
isbn_label_book_add.grid(row=3,column=0)
genre_label_book_add = tk.Label(add_book_frame,text='Book Genre',anchor='w')
genre_label_book_add.grid(row=4,column=0)

title_entry_book_add = tk.Entry(add_book_frame)
title_entry_book_add.grid(row=1,column=1)
author_entry_book_add = tk.Entry(add_book_frame)
author_entry_book_add.grid(row=2,column=1)
isbn_entry_book_add = tk.Entry(add_book_frame)
isbn_entry_book_add.grid(row=3,column=1)
genre_entry_book_add = tk.Entry(add_book_frame)
genre_entry_book_add.grid(row=4,column=1)

cancel_book_add_button = tk.Button(add_book_frame, text='Cancel', command=cancel_book_add)
cancel_book_add_button.grid(row=5,column=0)
submit_book_add_button = tk.Button(add_book_frame, text='Add Book', command=add_book)
submit_book_add_button.grid(row=5,column=1)


# Add Borrowing page ---------------------------------------------------------------------------------------------------------------------------------------------------------
title_book_borrow = tk.Label(borrow_book_frame,text='Fill the form Below')
title_book_borrow.grid(row=0,column=0,columnspan=2,padx=40,pady=5)

student_name_label_book_borrow = tk.Label(borrow_book_frame,text='Student name',anchor='w')
student_name_label_book_borrow.grid(row=1,column=0)
student_id_label_book_borrow = tk.Label(borrow_book_frame,text='Student ID',anchor='w')
student_id_label_book_borrow.grid(row=2,column=0)
return_date_label_book_borrow = tk.Label(borrow_book_frame,text='Return Date',anchor='w')
return_date_label_book_borrow.grid(row=3,column=0)

student_name_entry_book_borrow = tk.Entry(borrow_book_frame)
student_name_entry_book_borrow.grid(row=1,column=1)
student_id_entry_book_borrow = tk.Entry(borrow_book_frame)
student_id_entry_book_borrow.grid(row=2,column=1)
return_date_entry_book_borrow = tk.Entry(borrow_book_frame)
return_date_entry_book_borrow.grid(row=3,column=1)

cancel_book_add_borrow = tk.Button(borrow_book_frame, text='Cancel', command=cancel_book_borrow)
cancel_book_add_borrow.grid(row=5,column=0)
submit_book_add_borrow = tk.Button(borrow_book_frame, text='Borrow Book', command=borrow_book)
submit_book_add_borrow.grid(row=5,column=1)


# Borrowed books page ---------------------------------------------------------------------------------------------------------------------------------------------------------
home_page_buton = tk.Button(borrowed_books_frame, text="<<< Home Page", command=lambda: show_frame(home_frame), padx=20, pady=5, bg='blue',fg='white')
home_page_buton.grid(row=0,column=0)

label2 = tk.Label(borrowed_books_frame, text="Manage Returns", font=("Arial", 18))
label2.grid(row=0,column=6,columnspan=2)

mark_returned_buton = tk.Button(borrowed_books_frame, text="Mark Returned", padx=25, pady=5, bg='blue',fg='white', anchor='w', command=mark_returned)
mark_returned_buton.grid(row=0,column=8)

View_all_books_button = tk.Button(borrowed_books_frame, text="View All books", padx=25, pady=5, bg='blue',fg='white', anchor='w', command=lambda: show_frame(all_books_frame))
View_all_books_button.grid(row=0,column=9)

transaction_tree = ttk.Treeview(borrowed_books_frame, columns=('ID', 'Student Name', 'Student ID', 'Book ID', 'Borrow Date', 'Due Date', 'Return Date', 'Returned'), show='headings')
transaction_tree.heading('ID', text='ID')
transaction_tree.heading('Student Name', text='Student Name')
transaction_tree.heading('Student ID', text='Student ID')
transaction_tree.heading('Book ID', text='Book ID')
transaction_tree.heading('Borrow Date', text='Borrow Date')
transaction_tree.heading('Due Date', text='Due Date')
transaction_tree.heading('Return Date', text='Return Date')
transaction_tree.heading('Returned', text='Returned')
transaction_tree.grid(row=1,column=0,columnspan=10)
refresh_transactions()


# Show the initial frame
show_frame(home_frame)

root.mainloop()
