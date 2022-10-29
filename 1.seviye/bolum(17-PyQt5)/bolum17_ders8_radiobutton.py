import sys
from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QLabel, QPushButton, QVBoxLayout


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radio_yazi = QLabel("seç birini")
        self.radiobutton1 = QRadioButton("ali")
        self.radiobutton2 = QRadioButton("veli")
        self.radiobutton3 = QRadioButton("ayşe")
        self.yazi_alani = QLabel("")
        self.buton = QPushButton("tıkla")

        v_box = QVBoxLayout()

        v_box.addWidget(self.radio_yazi)
        v_box.addWidget(self.radiobutton1)
        v_box.addWidget(self.radiobutton2)
        v_box.addWidget(self.radiobutton3)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)

        self.setWindowTitle("ders 8 radiobutten")
        self.buton.clicked.connect(lambda: self.click(self.radiobutton1, self.radiobutton2, self.radiobutton3))
        self.show()

    def click(self, a, b, c):
        if a.isChecked():
            self.yazi_alani.setText(a.text() + "yi seçtin")
        if b.isChecked():
            self.yazi_alani.setText(b.text() + " yi seçtin")
        if c.isChecked():
            self.yazi_alani.setText(c.text() + " yi seçtin")


app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
