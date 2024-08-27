import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Sign In Form")
        self.setGeometry(300, 300, 400, 250)

        # Set overall layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # Add Widgets
        title = qtw.QLabel('Sign In Form')
        title.setFont(qtg.QFont('Helvetica', 24, qtg.QFont.Bold))
        title.setAlignment(qtc.Qt.AlignCenter)

        f_name = qtw.QLineEdit(self)
        f_name.setPlaceholderText("Enter your first name")
        f_name.setFont(qtg.QFont('Helvetica', 12))
        f_name.setStyleSheet("padding: 5px; border: 1px solid gray; border-radius: 1px;")

        l_name = qtw.QLineEdit(self)
        l_name.setPlaceholderText("Enter your last name")
        l_name.setFont(qtg.QFont('Helvetica', 12))
        l_name.setStyleSheet("padding: 5px; border: 1px solid gray; border-radius: 1px;")

        submit_button = qtw.QPushButton("Submit")
        submit_button.setFont(qtg.QFont('Helvetica', 12))
        submit_button.setStyleSheet(
            "background-color: purple; color: white; padding: 8px 15px; border-radius: 2px;"
        )
        submit_button.clicked.connect(self.submit)

        # Add rows to the form layout
        form_layout.addRow(title)
        form_layout.addRow("First name:", f_name)
        form_layout.addRow("Last name:", l_name)
        form_layout.addRow(submit_button)

        self.message_label = qtw.QLabel('')
        form_layout.addRow(self.message_label)

        # Adjust the spacing between form elements
        form_layout.setVerticalSpacing(15)

        # Show the app
        self.show()

    def submit(self):
        self.message_label.setText(
            f'You are signed in as {self.findChild(qtw.QLineEdit, "").text()} {self.findChild(qtw.QLineEdit, "", 1).text()}'
        )
        self.message_label.setFont(qtg.QFont('Helvetica', 12))
        self.message_label.setStyleSheet("color: purple; font-weight: bold;")
        self.message_label.adjustSize()

app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()
