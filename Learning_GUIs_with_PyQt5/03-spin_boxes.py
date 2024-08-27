import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Spin Boxes")

        # Set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        my_label = qtw.QLabel("Pick a value in the spin box below:")
        # Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 16))
        self.layout().addWidget(my_label)
        
        # Create an Spin box: Use QDoubleSpinBox for floating numners
        my_spin = qtw.QSpinBox(self,
                               value=10,
                               maximum=100,
                               minimum=0,
                               singleStep=5,
                               prefix='#',
                               suffix=' kgs')
        # Change font size of the spin box
        my_spin.setFont(qtg.QFont('Helvetica', 14))
        # Put combo box on screen
        self.layout().addWidget(my_spin)

        # Create a botton
        my_button = qtw.QPushButton("Press Me!",
                                    clicked = lambda: press_it())
        my_button.setFont(qtg.QFont('Helvetica', 16))
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            label_1 = qtw.QLabel(f'You picked {my_spin.value()} kgs')
            label_1.setFont(qtg.QFont('Helvetica', 16))
            self.layout().addWidget(label_1)

app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()