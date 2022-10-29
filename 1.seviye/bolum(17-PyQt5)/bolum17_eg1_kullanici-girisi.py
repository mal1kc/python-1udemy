import sys
from PyQt5 import QtWidgets
import sqlite3


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.db_connect()
        self.init_ui()
        self.setWindowTitle("User Login")

    def db_connect(self):
        self.db_connection = sqlite3.connect("user_db.db")
        self.cursor = self.db_connection.cursor()
        self.cursor.execute("Create table if not exists users(username TEXT,password TEXT)")
        self.db_connection.commit()

    def init_ui(self):
        self.header = QtWidgets.QLabel("Welcome To User Login Panel")
        self.usarname = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.register_button = QtWidgets.QPushButton("Register")
        self.login_button = QtWidgets.QPushButton("Login")
        self.text_area = QtWidgets.QLabel("")

        h_box0 = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()
        h_box1 = QtWidgets.QHBoxLayout()

        h_box1.addWidget(self.register_button)
        h_box1.addStretch()
        h_box1.addWidget(self.login_button)

        v_box.addWidget(self.header)
        v_box.addStretch()
        v_box.addWidget(self.usarname)
        v_box.addWidget(self.password)
        v_box.addWidget(self.text_area)
        v_box.addLayout(h_box1)

        v_box.addStretch()

        h_box0.addStretch()
        h_box0.addLayout(v_box)
        h_box0.addStretch()

        self.setLayout(h_box0)
        self.register_button.clicked.connect(self.register)
        self.login_button.clicked.connect(self.login)
        self.show()

    def login(self):
        quiry = "SELECT * FROM users WHERE username = ? and password = ?"
        name = self.usarname.text()
        passw = self.password.text()

        self.cursor.execute(quiry, (name, passw))

        results = self.cursor.fetchall()
        if len(results) == 0:
            self.text_area.setText("boyle bir kullanıcı yok \n lütfen tekrar deneyiniz")
        else:
            self.text_area.setText("{} kullanıcı hesabına giris yaptınız".format(name))

    def register(self):
        quiry = "INSERT INTO users Values(?,?)"
        name = self.usarname.text()
        passw = self.password.text()
        self.cursor.execute(quiry, (name, passw))
        self.db_connection.commit()
        self.text_area.setText("{} kullanıcı hesabı basarıyla veritabanına eklendi".format(name))


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
