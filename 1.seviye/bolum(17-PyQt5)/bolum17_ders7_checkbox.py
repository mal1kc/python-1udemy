import sys
from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QLabel, QPushButton, QVBoxLayout


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.checkbox = QCheckBox("onaylıyorum")
        self.yazi_alani = QLabel("")
        self.buton = QPushButton("tıkla")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("ders 7 checkbox")
        self.buton.clicked.connect(lambda: self.click(self.checkbox.isChecked(), self.yazi_alani))
        self.show()

    def click(self, checkbox, yazi_alani):
        if checkbox:
            yazi_alani.setText("sen bunu onaylıyorsun")
        else:
            yazi_alani.setText("niye onaylamıyorsun")


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
