import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Text Boxes")

        # Set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        my_label = qtw.QLabel("Type something in the text box below:")
        # Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 16))
        self.layout().addWidget(my_label)
        
        # Create an Spin box: Use QDoubleSpinBox for floating numners
        my_text = qtw.QTextEdit(self,
                                # plainText="This is real text",
                                # html='<center><h1><em>This is PyQt5</em></h1></center>',
                                acceptRichText=False,
                                lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                                lineWrapColumnOrWidth=50,
                                placeholderText='Type something....',
                                readOnly=False,
                                
                               )
        # Change font size of the spin box
        my_text.setFont(qtg.QFont('Helvetica', 10))
        # Put combo box on screen
        self.layout().addWidget(my_text)

        # Create a botton
        my_button = qtw.QPushButton("Press Me!",
                                    clicked = lambda: press_it())
        my_button.setFont(qtg.QFont('Helvetica', 14))
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            label_1 = qtw.QLabel(f'You typed "{my_text.toPlainText()}"')
            label_1.setFont(qtg.QFont('Helvetica', 14))
            self.layout().addWidget(label_1)
            # Setting text in the box: my_text.setPlainText("You pressed the Button!")

app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()