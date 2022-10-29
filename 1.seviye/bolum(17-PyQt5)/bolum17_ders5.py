import sys
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self):
        self.yazi = QtWidgets.QLabel("henüz tıklanmadı")
        self.buton = QtWidgets.QPushButton("tıkla")

        self.say = 0

        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()

        v_box.addWidget(self.yazi)
        v_box.addWidget(self.buton)

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)

        self.buton.clicked.connect(self.clicked)

        self.show()

    def clicked(self):
        self.say += 1
        self.yazi.setText("butona {} kez tıklandı".format(self.say))


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
