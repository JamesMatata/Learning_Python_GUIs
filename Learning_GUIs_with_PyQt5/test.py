from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title Label
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(20, 0, 360, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setObjectName("title")

        # Line
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(15, 30, 370, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # Choose What to Do Label
        self.choose_what_to_do_label = QtWidgets.QLabel(self.centralwidget)
        self.choose_what_to_do_label.setGeometry(QtCore.QRect(20, 50, 360, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_what_to_do_label.setFont(font)
        self.choose_what_to_do_label.setObjectName("choose_what_to_do_label")

        # First Combo Box (Choose What to Do)
        self.choose_what_to_do_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.choose_what_to_do_combo_box.setGeometry(QtCore.QRect(20, 80, 360, 35))
        self.choose_what_to_do_combo_box.setCurrentText("")
        self.choose_what_to_do_combo_box.setObjectName("choose_what_to_do_combo_box")
        self.choose_what_to_do_combo_box.setStyleSheet('font-size: 14px;')

        # Specify Label
        self.specify_label = QtWidgets.QLabel(self.centralwidget)
        self.specify_label.setGeometry(QtCore.QRect(20, 130, 360, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.specify_label.setFont(font)
        self.specify_label.setObjectName("specify_label")

        # Second Combo Box (Specify)
        self.specify_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.specify_combo_box.setGeometry(QtCore.QRect(20, 160, 360, 35))
        self.specify_combo_box.setObjectName("specify_combo_box")
        self.specify_combo_box.setStyleSheet('font-size: 14px;')

        # Frame for Parameters
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 200, 360, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Calculate Button
        self.calculate_button = QtWidgets.QPushButton(self.frame, clicked=lambda: self.calculate())
        self.calculate_button.setGeometry(QtCore.QRect(10, 110, 340, 41))
        self.calculate_button.setObjectName("calculate_button")

        # Inner Frame for Parameter Inputs
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 9, 340, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        # Parameter 1 Label
        self.parameter_1_label = QtWidgets.QLabel(self.frame_2)
        self.parameter_1_label.setGeometry(QtCore.QRect(0, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.parameter_1_label.setFont(font)
        self.parameter_1_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.parameter_1_label.setObjectName("parameter_1_label")

        # Parameter 1 Input
        self.parameter_1_text_edit = QtWidgets.QTextEdit(self.frame_2)
        self.parameter_1_text_edit.setGeometry(QtCore.QRect(105, 10, 230, 30))
        self.parameter_1_text_edit.setObjectName("parameter_1_text_edit")

        # Parameter 2 Label
        self.parameter_2_label = QtWidgets.QLabel(self.frame_2)
        self.parameter_2_label.setGeometry(QtCore.QRect(0, 50, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.parameter_2_label.setFont(font)
        self.parameter_2_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.parameter_2_label.setObjectName("parameter_2_label")

        # Parameter 2 Input
        self.parameter_2_text_edit = QtWidgets.QTextEdit(self.frame_2)
        self.parameter_2_text_edit.setGeometry(QtCore.QRect(105, 50, 230, 30))
        self.parameter_2_text_edit.setObjectName("parameter_2_text_edit")

        # Parameter 3 Label
        self.parameter_3_label = QtWidgets.QLabel(self.frame_2)
        self.parameter_3_label.setGeometry(QtCore.QRect(0, 90, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.parameter_3_label.setFont(font)
        self.parameter_3_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.parameter_3_label.setObjectName("parameter_3_label")

        # Parameter 3 Input
        self.parameter_3_text_edit = QtWidgets.QTextEdit(self.frame_2)
        self.parameter_3_text_edit.setGeometry(QtCore.QRect(105, 90, 230, 30))
        self.parameter_3_text_edit.setObjectName("parameter_3_text_edit")

        # Output Label
        self.output = QtWidgets.QLabel(self.frame)
        self.output.setGeometry(QtCore.QRect(10, 170, 340, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output.setFont(font)
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect signals to slots
        self.choose_what_to_do_combo_box.currentIndexChanged.connect(self.updateSpecifyComboBox)
        self.specify_combo_box.currentIndexChanged.connect(self.updateParameterFields)

        # Initialize the combo box options
        self.initializeComboBoxes()

    def initializeComboBoxes(self):
        main_items = [('Area', 'area'), ('Volume', 'volume')]
        for item, data in main_items:
            self.choose_what_to_do_combo_box.addItem(item, data)
        
        # Trigger the first update
        self.updateSpecifyComboBox()

    def updateSpecifyComboBox(self):
        self.specify_combo_box.clear()
        selected_option = self.choose_what_to_do_combo_box.currentText()

        if selected_option == 'Area':
            sub_main_items = [('Rectangle', 'r'), ('Triangle', 't'), ('Circle', 'c'), ('Trapezium', 'tr'), ('Rhombus', 'rh'), ('Trapezium', 'tr') ]
        else:
            sub_main_items = [('Sphere', 's'), ('Cylinder', 'cy'), ('Cuboid', 'cu')]

        for item, data in sub_main_items:
            self.specify_combo_box.addItem(item, data)
        
        # Trigger the parameter field update for the first item
        self.updateParameterFields()

    def updateParameterFields(self):
        selected_option = self.specify_combo_box.currentText()

        if selected_option == 'Rectangle':
            self.parameter_1_label.setText("Length:")
            self.parameter_2_label.setText("Width:")
            self.parameter_2_text_edit.setVisible(True)
            self.parameter_2_label.setVisible(True)
        elif selected_option == 'Triangle':
            self.parameter_1_label.setText("Base:")
            self.parameter_2_label.setText("Height:")
            self.parameter_2_text_edit.setVisible(True)
            self.parameter_2_label.setVisible(True)
        elif selected_option == 'Circle':
            self.parameter_1_label.setText("Radius:")
            self.parameter_2_text_edit.setVisible(False)
            self.parameter_2_label.setVisible(False)
            self.parameter_3_label.setVisible(False)
        elif selected_option == 'Trapezium':
            self.parameter_1_label.setText("Base 1:")
            self.parameter_2_label.setText("Base 2:")
            self.parameter_3_label.setText("Height:")
            self.parameter_2_text_edit.setVisible(True)
            self.parameter_2_label.setVisible(True)
            self.parameter_3_label.setVisible(True)
        elif selected_option == 'Sphere':
            self.parameter_1_label.setText("Radius:")
            self.parameter_2_text_edit.setVisible(False)
            self.parameter_2_label.setVisible(False)
        elif selected_option == 'Cylinder':
            self.parameter_1_label.setText("Radius:")
            self.parameter_2_label.setText("Height:")
            self.parameter_2_text_edit.setVisible(True)
            self.parameter_2_label.setVisible(True)
        elif selected_option == 'Cuboid':
            self.parameter_1_label.setText("Length:")
            self.parameter_2_label.setText("Width:")
            self.parameter_2_text_edit.setVisible(True)
            self.parameter_2_label.setVisible(True)

    def calculate(self):
        selected_option = self.specify_combo_box.currentText()

        if selected_option == 'Rectangle':
            area = int(self.parameter_1_text_edit.toPlainText())*int(self.parameter_2_text_edit.toPlainText())
            self.output.setText(str(area))
            
        elif selected_option == 'Triangle':
            area = 0.5*int(self.parameter_1_text_edit.toPlainText())*int(self.parameter_2_text_edit.toPlainText())
            self.output.setText(str(area))

        elif selected_option == 'Circle':
            area = int(self.parameter_1_text_edit.toPlainText())**2*3.14
            self.output.setText(str(area))
        elif selected_option == 'Trapezium':
            self.parameter_1_label.setText("Base 1:")
            self.parameter_2_label.setText("Base 2:")
            self.parameter_2_text_edit.setVisible(True)
            self.parameter_2_label.setVisible(True)
        elif selected_option == 'Sphere':
            self.parameter_1_label.setText("Radius:")
            self.parameter_2_text_edit.setVisible(False)
            self.parameter_2_label.setVisible(False)
        elif selected_option == 'Cylinder':
            self.parameter_1_label.setText("Radius:")
            self.parameter_2_label.setText("Height:")
            self.parameter_2_text_edit.setVisible(True)
            self.parameter_2_label.setVisible(True)
        elif selected_option == 'Cuboid':
            self.parameter_1_label.setText("Length:")
            self.parameter_2_label.setText("Width:")
            self.parameter_2_text_edit.setVisible(True)
            self.parameter_2_label.setVisible(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Area and Volume Finder"))
        self.title.setText(_translate("MainWindow", "Area, Surface Area, and Volume Finder"))
        self.choose_what_to_do_label.setText(_translate("MainWindow", "Choose what to find:"))
        self.specify_label.setText(_translate("MainWindow", "Specify:"))
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))
        self.output.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
