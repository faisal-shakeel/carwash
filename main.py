import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QStyle, \
    QDialog
from PyQt5.QtGui import QIcon
import sqlite3
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot

class Person:

      def __init__(self, fullname, username,password,address,email,telephone,washcard):
        self.name = fullname
        self.username = username
        self.password = password
        self.address = address
        self.email = email
        self.telephone = telephone
        self.washcard = washcard




class Employee(Person):
    def __init__(self, fullname, username,password,address,email,telephone,washcard,status,empid):
        super().__init__(fullname, username,password,address,email,telephone,washcard)
        self.status = status
        self.empid = empid

class UserMain(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = 'User Main'
        self.left = 200
        self.top = 200
        self.width = 370
        self.height = 400
        self.window2()

    def window2(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        # ---------
        # Create a button in the window
        self.signbutton = QPushButton('View Information', self)
        self.signbutton.move(140, 90)
        # self.signbutton.clicked.connect(self.signupfunc)

        #  ------------

        self.signbutton = QPushButton('Purchase Product', self)
        self.signbutton.move(140, 30)
        # self.signbutton.clicked.connect(self.signupfunc)

        # --------------

        self.signbutton = QPushButton('Top up', self)
        self.signbutton.move(140, 60)
        # self.signbutton.clicked.connect(self.signupfunc)
        
        # connect button to function on_click
        # self.regbutton.clicked.connect(self.on_clickreg)
        # self.signbutton.clicked.connect(self.on_clicksign)
        self.show()



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'CAR WASH'
        self.left = 200
        self.top = 200
        self.width = 370
        self.height = 400
        self.window()

    def window(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        # ---------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Full Name:")
        self.label.move(40, 20)

        self.ftextbox = QLineEdit(self)
        self.ftextbox.move(40, 50)
        self.ftextbox.resize(90, 25)
        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("User Name:")
        self.label.move(220, 20)

        self.ltextbox = QLineEdit(self)
        self.ltextbox.move(220, 50)
        self.ltextbox.resize(90, 25)

        # ----------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Password:")
        self.label.move(40, 80)

        self.stextbox = QLineEdit(self)
        self.stextbox.move(40, 110)
        self.stextbox.resize(90, 25)

        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Address:")
        self.label.move(220, 80)

        self.ctextbox = QLineEdit(self)
        self.ctextbox.move(220, 110)
        self.ctextbox.resize(90, 25)

        # --------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Telephone:")
        self.label.move(40, 140)

        self.sstextbox = QLineEdit(self)
        self.sstextbox.move(40, 170)
        self.sstextbox.resize(90, 25)

        # ----------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Email:")
        self.label.move(220, 140)

        self.etextbox = QLineEdit(self)
        self.etextbox.move(220, 170)
        self.etextbox.resize(90, 25)

        # ------------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Wash-Card No:")
        self.label.move(40, 200)

        self.ttextbox = QLineEdit(self)
        self.ttextbox.move(40, 230)
        self.ttextbox.resize(90, 25)

        # ------------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Employee No:")
        self.label.move(220, 200)

        self.ettextbox = QLineEdit(self)
        self.ettextbox.move(220, 230)
        self.ettextbox.resize(90, 25)
        self.ettextbox.setText("N/A")

        # ------------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Status:")
        self.label.move(40, 260)

        self.sttextbox = QLineEdit(self)
        self.sttextbox.move(40, 290)
        self.sttextbox.resize(90, 25)
        self.sttextbox.setText("N/A")

        # Create a button in the window
        self.regbutton = QPushButton('Register', self)
        self.regbutton.move(40, 330)
        # Create a button in the window
        self.signbutton = QPushButton('Sign In', self)
        self.signbutton.move(220, 330)
        # connect button to function on_click
        self.regbutton.clicked.connect(self.on_clickreg)
        self.signbutton.clicked.connect(self.on_clicksign)
        self.show()

    @pyqtSlot()
    def on_clickreg(self):
        Fullname = self.ftextbox.text(),
        Username = self.ltextbox.text(),
        Password = self.stextbox.text(),
        Address = self.ctextbox.text(),
        washcard = self.ttextbox.text(),
        telephone = self.sstextbox.text(),
        email = self.etextbox.text()
        emplno = self.ettextbox.text()
        status = self.sttextbox.text()
        f = open("webuser.txt", "a")
        # open and read the file after the appending:


        if(emplno=="N/A"):
            user=Person(Fullname, Username,Password,Address,email,telephone,washcard)
            userlist=(user.name,user.password,"/n")
            f.writelines(userlist) # error here
            f.close()
            f = open("webuser.txt", "r")
            print(f.read())
        else:
            emp=Person(Fullname, Username,Password,Address,email,telephone,washcard,status,emplno)

    def on_clicksign(self):
        self.cams = Signinwindow("self.lineEdit2.text()")
        self.cams.show()
        
        self.close()


class Signinwindow(QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Sign In')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_FileDialogInfoView))
        self.sign()

    def sign(self):
        # ---------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("User Name:")
        self.label.move(40, 20)

        self.ftextbox = QLineEdit(self)
        self.ftextbox.move(40, 50)
        self.ftextbox.resize(90, 25)
        # ------------
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Password:")
        self.label.move(220, 20)

        self.ltextbox = QLineEdit(self)
        self.ltextbox.move(220, 50)
        self.ltextbox.resize(90, 25)

        # Create a button in the window
        self.signbutton = QPushButton('Sign In', self)
        self.signbutton.move(140, 100)
        self.signbutton.clicked.connect(self.signupfunc)
        

    def signupfunc(self):
        self.cams = UserMain()
        self.cams.show()
        self.show()
        self.close()

    def goMainWindow(self):
        self.cams = App()
        self.cams.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
