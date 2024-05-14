import sys
from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")

        dosya_ac = QAction("Dosya Aç", self)
        dosya_ac.setShortcut("Ctrl+O")
        dosya_kaydet = QAction("Dosya kaydet", self)
        dosya_kaydet.setShortcut("Ctrl+S")
        cikis = QAction("Çıkış", self)
        cikis.setShortcut("Ctrl+Q")

        ara_ve_degistir = duzenle.addMenu("Ara ve Değiştir")

        temizle = QAction("Temizle", self)
        ara = QAction("Ara", self)
        degistir = QAction("Değiştir", self)

        ara_ve_degistir.addActions((ara, degistir))

        duzenle.addAction(temizle)

        dosya.addActions((dosya_ac, dosya_kaydet, cikis))

        cikis.triggered.connect(self.cikis_yap)

        dosya.triggered.connect(self.response)

        self.setWindowTitle("Menüler")
        self.show()

    def cikis_yap(self):
        qApp.quit()

    def response(self, action):
        if action.text() == "Dosya Aç":
            print("dosya aç a basıldı")
        elif action.text() == "Dosya kaydet":
            print("dosya kaydet e basıldı")
        elif action.text() == "Çıkış":
            print("Çıkış a basıldı")


app = QApplication(sys.argv)

menu = Menu()

sys.exit((app.exec_()))
