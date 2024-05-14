import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QRadioButton, QVBoxLayout, QFileDialog, \
    QPushButton, QHBoxLayout


class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.text_area = QTextEdit()
        self.clear_button = QPushButton("Clear")
        self.open = QPushButton("open")
        self.save = QPushButton("save")

        h_box = QHBoxLayout()
        v_box = QVBoxLayout()

        h_box.addWidget(self.clear_button)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)

        v_box.addWidget(self.text_area)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("Notepadd")
        self.clear_button.clicked.connect(self.clear_text)
        self.open.clicked.connect(self.open_file)
        self.save.clicked.connect(self.save_file)
        self.show()

    def clear_text(self):
        self.text_area.clear()

    def open_file(self):
        dosya_ismi = QFileDialog.getOpenFileName(self, "Dosyayı Aç", os.getenv("HOME"))
        with open(dosya_ismi[0], "r") as file:
            self.text_area.setText(file.read())

    def save_file(self):
        dosya_ismi = QFileDialog.getSaveFileName(self, "Dosyayı kaydet", os.getenv("HOME"))
        with open(dosya_ismi[0], "w") as file:
            file.write(self.text_area.toPlainText())


app = QApplication(sys.argv)
notepad = Notepad()
sys.exit(app.exec_())
