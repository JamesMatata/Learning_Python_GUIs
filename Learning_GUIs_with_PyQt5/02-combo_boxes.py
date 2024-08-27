import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Combo Boxes")

        # Set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        my_label = qtw.QLabel("Pick a fruit from the list below:")
        # Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)
        
        # Create an Combo box
        # We use editable attribute to make the item editable
        my_combo = qtw.QComboBox(self, 
                                 editable=True,
                                 insertPolicy=qtw.QComboBox.InsertAtTop
                                 )
        
        # Add items to the combo box
        items = [('Oranges','O'), ('Mangoes', ''), ('Lemons', ''), ('Watermelons', ''), ('Apples','')]
        for item,data in items:
            my_combo.addItem(item,data)

        # Put combo box on screen
        self.layout().addWidget(my_combo)

        # Create a botton
        my_button = qtw.QPushButton("Press Me!",
                                    clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            label_1 = qtw.QLabel(f'You picked {my_combo.currentText()}')
            label_2 = qtw.QLabel(f'The data of the item you picked is {my_combo.currentData()}')
            label_3 = qtw.QLabel(f'The index of the item you picked is {my_combo.currentIndex()}')
            self.layout().addWidget(label_1)
            self.layout().addWidget(label_2)
            self.layout().addWidget(label_3)

app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()