import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget, QTreeWidget, QTreeWidgetItem, QMessageBox
from PyQt5.QtGui import QFont
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
            school TEXT,
            borrowed_books INTEGER)''')

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

class LibrarySystem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Library Management System")
        self.setGeometry(100, 100, 800, 600)

        # Apply a stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #333;
            }
            QPushButton {
                font-size: 16px;
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QTreeWidget {
                font-size: 14px;
                border: 1px solid #ccc;
                background-color: white;
            }
            QTreeWidget::item:selected {
                background-color: #007BFF;
                color: white;
            }
        """)

        # Central widget to hold different frames
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Layout
        self.layout = QVBoxLayout(self.central_widget)

        # StackedWidget to switch between different views
        self.stack = QStackedWidget()
        self.layout.addWidget(self.stack)

        # Home Page
        self.home_page = QWidget()
        self.home_layout = QVBoxLayout()
        self.home_page.setLayout(self.home_layout)

        self.library_label = QLabel("lastKing Library\n")
        self.home_layout.addWidget(self.library_label)

        self.manage_books_button = QPushButton("Manage Books")
        self.manage_books_button.clicked.connect(self.show_books_page)
        self.home_layout.addWidget(self.manage_books_button)

        self.borrowed_books_button = QPushButton("Borrowed Books")
        self.borrowed_books_button.clicked.connect(self.show_borrowed_books_page)
        self.home_layout.addWidget(self.borrowed_books_button)

        self.view_students_button = QPushButton("View Students")
        self.view_students_button.clicked.connect(self.show_students_page)
        self.home_layout.addWidget(self.view_students_button)

        self.stack.addWidget(self.home_page)

        # Books Management Page
        self.books_page = QWidget()
        self.books_layout = QVBoxLayout()
        self.books_page.setLayout(self.books_layout)

        self.home_button = QPushButton("<<< Home Page")
        self.home_button.clicked.connect(self.show_home_page)
        self.books_layout.addWidget(self.home_button)

        self.book_tree = QTreeWidget()
        self.book_tree.setHeaderLabels(["ID", "Title", "Author", "ISBN", "Genre", "Available"])
        self.books_layout.addWidget(self.book_tree)

        self.add_book_button = QPushButton("Add Book")
        self.add_book_button.clicked.connect(self.add_book)
        self.books_layout.addWidget(self.add_book_button)

        self.stack.addWidget(self.books_page)

        # Borrowed Books Page
        self.borrowed_books_page = QWidget()
        self.borrowed_books_layout = QVBoxLayout()
        self.borrowed_books_page.setLayout(self.borrowed_books_layout)

        self.home_button_borrowed = QPushButton("<<< Home Page")
        self.home_button_borrowed.clicked.connect(self.show_home_page)
        self.borrowed_books_layout.addWidget(self.home_button_borrowed)

        self.transaction_tree = QTreeWidget()
        self.transaction_tree.setHeaderLabels(["ID", "Student Name", "Student ID", "Book ID", "Borrow Date", "Due Date", "Return Date", "Returned"])
        self.borrowed_books_layout.addWidget(self.transaction_tree)

        self.mark_returned_button = QPushButton("Mark Returned")
        self.mark_returned_button.clicked.connect(self.mark_returned)
        self.borrowed_books_layout.addWidget(self.mark_returned_button)

        self.stack.addWidget(self.borrowed_books_page)

        # Load initial data
        self.refresh_books()
        self.refresh_transactions()

    def show_home_page(self):
        self.stack.setCurrentWidget(self.home_page)

    def show_books_page(self):
        self.stack.setCurrentWidget(self.books_page)

    def show_borrowed_books_page(self):
        self.stack.setCurrentWidget(self.borrowed_books_page)

    def show_students_page(self):
        pass  # Implement as needed

    def refresh_books(self):
        self.book_tree.clear()
        c.execute("SELECT * FROM books")
        books = c.fetchall()
        for book in books:
            QTreeWidgetItem(self.book_tree, [str(field) for field in book])

    def refresh_transactions(self):
        self.transaction_tree.clear()
        c.execute("SELECT * FROM transactions")
        transactions = c.fetchall()
        for transaction in transactions:
            QTreeWidgetItem(self.transaction_tree, [str(field) for field in transaction])

    def add_book(self):
        title, author, isbn, genre = "Sample Title", "Sample Author", "123456", "Genre"
        if title and author and isbn and genre:
            c.execute("INSERT INTO books (title, author, isbn, genre, available) VALUES (?, ?, ?, ?, 1)", (title, author, isbn, genre))
            conn.commit()
            QMessageBox.information(self, "Success", "Book added successfully!")
            self.refresh_books()

    def mark_returned(self):
        selected_item = self.transaction_tree.currentItem()
        if selected_item:
            transaction_id = selected_item.text(0)
            return_date = datetime.now().strftime('%Y-%m-%d')
            c.execute("UPDATE transactions SET return_date=?, returned=1 WHERE id=?", (return_date, transaction_id))
            book_id = selected_item.text(3)
            c.execute("UPDATE books SET available=1 WHERE id=?", (book_id,))
            conn.commit()
            QMessageBox.information(self, "Success", "Book marked as returned!")
            self.refresh_transactions()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LibrarySystem()
    window.show()
    sys.exit(app.exec_())
