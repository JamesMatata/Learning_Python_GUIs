from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    count = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 126)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.next_command_link_button = QtWidgets.QCommandLinkButton(self.centralwidget, clicked=lambda: self.increament())
        self.next_command_link_button.setGeometry(QtCore.QRect(10, 40, 161, 41))
        self.next_command_link_button.setObjectName("next_command_link_button")
        self.next_label = QtWidgets.QLabel(self.centralwidget)
        self.next_label.setGeometry(QtCore.QRect(190, 22, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.next_label.setFont(font)
        self.next_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.next_label.setIndent(0)
        self.next_label.setObjectName("next_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def increament(self):
        self.count += 1
        self.next_label.setText(str(self.count))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_command_link_button.setText(_translate("MainWindow", "Increase Counter"))
        self.next_label.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
