from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

conn = sqlite3.connect('todo_list.db')

c = conn.cursor()

c.execute("""CREATE TABLE if not exists todo_list(
            task text)""")

conn.commit()

conn.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 473)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_task_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_it())
        self.add_task_button.setGeometry(QtCore.QRect(10, 50, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_task_button.setFont(font)
        self.add_task_button.setObjectName("add_task_button")
        self.remove_task_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.remove_it())
        self.remove_task_button.setGeometry(QtCore.QRect(135, 50, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.remove_task_button.setFont(font)
        self.remove_task_button.setObjectName("remove_task_button")
        self.clear_list_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_it())
        self.clear_list_button.setGeometry(QtCore.QRect(260, 50, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clear_list_button.setFont(font)
        self.clear_list_button.setObjectName("clear_list_button")
        self.task_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.task_entry.setGeometry(QtCore.QRect(10, 5, 515, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.task_entry.setFont(font)
        self.task_entry.setObjectName("task_entry")
        self.tasks_list = QtWidgets.QListWidget(self.centralwidget)
        self.tasks_list.setGeometry(QtCore.QRect(10, 95, 515, 330))
        self.tasks_list.setObjectName("tasks_list")
        self.save_to_database_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.save_it())
        self.save_to_database_button.setGeometry(QtCore.QRect(385, 50, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_to_database_button.setFont(font)
        self.save_to_database_button.setObjectName("save_to_database_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Grab all the items from the database
        self.grab_all()

    def grab_all(self):
        conn = sqlite3.connect('todo_list.db')

        c = conn.cursor()

        c.execute("SELECT * FROM todo_list")
        tasks = c.fetchall()

        conn.commit()

        conn.close()

        for task in tasks:
            self.tasks_list.addItem(str(task[0]))

    def add_it(self):
        task = self.task_entry.text()
        if task:
            self.tasks_list.addItem(task)
            self.task_entry.setText("")
        else:
            pass

    def remove_it(self):
        selected = self.tasks_list.currentRow()
        self.tasks_list.takeItem(selected)

    def clear_it(self):
        self.tasks_list.clear()

    def save_it(self):
        conn = sqlite3.connect('todo_list.db')

        c = conn.cursor()

        # Delete everything in the database table
        c.execute('DELETE FROM todo_list;',)

        items = []
        for index in range(self.tasks_list.count()):
            items.append(self.tasks_list.item(index))

        for item in items:
            c.execute("INSERT INTO todo_list VALUES (:item)",
                      {
                          'item': item.text(),
                      }
                      )
        
        conn.commit()

        conn.close()

        # Add popup message
        msg = QMessageBox()
        msg.setWindowTitle("Saved to Database!")
        msg.setText("Your Todo List has been saved")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_task_button.setText(_translate("MainWindow", "Add Task"))
        self.remove_task_button.setText(_translate("MainWindow", "Remove Task"))
        self.clear_list_button.setText(_translate("MainWindow", "Clear List"))
        self.save_to_database_button.setText(_translate("MainWindow", "Save To Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
