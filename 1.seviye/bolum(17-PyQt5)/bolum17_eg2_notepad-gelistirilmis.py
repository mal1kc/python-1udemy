import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QVBoxLayout, QFileDialog, QMainWindow, QAction, qApp

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_area = QTextEdit()
        v_box = QVBoxLayout()

        v_box.addWidget(self.text_area)

        self.setLayout(v_box)

    def clear_text(self):
        self.text_area.clear()

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, "open f", os.getenv("HOME"))
        with open(file_name[0], "r") as f:
            self.text_area.setText(f.read())

    def save_file(self):
        file_name = QFileDialog.getSaveFileName(self, "save file", os.getenv("HOME"))
        with open(file_name[0], "w") as f:
            f.write(self.text_area.toPlainText())


class Menu(QMainWindow):

    def __init__(self):
        super(Menu, self).__init__()

        self.window = Notepad()

        self.setCentralWidget(self.window)

        self.window.setWindowTitle("Text Editor")

        self.create_menus()

        self.show()

    def create_menus(self):
        menubar = self.menuBar()

        file = menubar.addMenu("file")
        edit = menubar.addMenu("edit")

        openfile = QAction("open file", self)
        openfile.setShortcut("Ctrl+O")
        savefile = QAction("save file", self)
        savefile.setShortcut("Ctrl+S")
        close = QAction("close", self)
        close.setShortcut("Ctrl+Q")

        file.addActions((openfile, savefile, close))

        cleartext = QAction("clear text", self)
        cleartext.setShortcut("Ctrl+D")

        edit.addAction(cleartext)

        file.triggered.connect(self.response)
        edit.triggered.connect(self.response)

    def response(self, action):
        if action.text() == "open file":
            self.window.open_file()
        elif action.text() == "save file":
            self.window.save_file()
        elif action.text() == "close":
            self.window.save_file()
            qApp.exit()
        elif action.text() == "clear text":
            self.window.clear_text()


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
