# import sys
# from PyQt5.QtCore import Qt, QPoint
# from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog
# from PyQt5.QtGui import QPixmap, QPainter, QPen
#
#
# class Menu(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.drawing = False
#         self.lastPoint = QPoint()
#         self.image = QPixmap(QFileDialog.getOpenFileName(self,"open iamge to draw")[0])
#         self.setGeometry(100, 100, 500, 300)
#         self.resize(self.image.width(), self.image.height())
#         self.show()
#
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.drawPixmap(self.rect(), self.image)
#
#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.drawing = True
#             self.lastPoint = event.pos()
#
#     def mouseMoveEvent(self, event):
#         if event.buttons() and Qt.LeftButton and self.drawing:
#             painter = QPainter(self.image)
#             painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
#             painter.drawLine(self.lastPoint, event.pos())
#             self.lastPoint = event.pos()
#             self.update()
#
#     def mouseReleaseEvent(self, event):
#         if event.button == Qt.LeftButton:
#             self.drawing = False
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainMenu = Menu()
#     sys.exit(app.exec_())
import io
import os

from PIL import Image, ImageFilter, ImageQt, ImageShow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_Ui(MainWindow)
        self.iscropped = False

    def init_Ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(825, 605))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 805, 602))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.main_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.main_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_horizontalLayout.setObjectName("main_horizontalLayout")
        self.image_box = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image_box.setText("")
        self.image_box.setPixmap(QtGui.QPixmap("kekw.png"))
        self.image_box.setObjectName("image_box")
        self.main_horizontalLayout.addWidget(self.image_box)
        self.verticalLayout_sidebig = QtWidgets.QVBoxLayout()
        self.verticalLayout_sidebig.setObjectName("verticalLayout_sidebig")
        self.verticalLayout_points = QtWidgets.QVBoxLayout()
        self.verticalLayout_points.setObjectName("verticalLayout_points")
        self.verticalLayout_select = QtWidgets.QVBoxLayout()
        self.verticalLayout_select.setObjectName("verticalLayout_select")
        self.horizontalLayout_selectpoint_t = QtWidgets.QHBoxLayout()
        self.horizontalLayout_selectpoint_t.setObjectName("horizontalLayout_selectpoint_t")
        self.select_point_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_point_text.sizePolicy().hasHeightForWidth())
        self.select_point_text.setSizePolicy(sizePolicy)
        self.select_point_text.setObjectName("select_point_text")
        self.horizontalLayout_selectpoint_t.addWidget(self.select_point_text)
        self.verticalLayout_select.addLayout(self.horizontalLayout_selectpoint_t)
        self.horizontalLayout_select_points_buttpns = QtWidgets.QHBoxLayout()
        self.horizontalLayout_select_points_buttpns.setObjectName("horizontalLayout_select_points_buttpns")
        self.pointselect1_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointselect1_button.sizePolicy().hasHeightForWidth())
        self.pointselect1_button.setSizePolicy(sizePolicy)
        self.pointselect1_button.setObjectName("pointselect1_button")
        self.horizontalLayout_select_points_buttpns.addWidget(self.pointselect1_button)
        self.pointselect2_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointselect2_button.sizePolicy().hasHeightForWidth())
        self.pointselect2_button.setSizePolicy(sizePolicy)
        self.pointselect2_button.setObjectName("pointselect2_button")
        self.horizontalLayout_select_points_buttpns.addWidget(self.pointselect2_button)
        self.verticalLayout_select.addLayout(self.horizontalLayout_select_points_buttpns)
        self.verticalLayout_points.addLayout(self.verticalLayout_select)
        self.horizontalLayout_point1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_point1.setObjectName("horizontalLayout_point1")
        self.point1_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point1_text.sizePolicy().hasHeightForWidth())
        self.point1_text.setSizePolicy(sizePolicy)
        self.point1_text.setObjectName("point1_text")
        self.horizontalLayout_point1.addWidget(self.point1_text)
        self.point1_x = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point1_x.sizePolicy().hasHeightForWidth())
        self.point1_x.setSizePolicy(sizePolicy)
        self.point1_x.setMinimumSize(QtCore.QSize(20, 20))
        self.point1_x.setObjectName("point1_x")
        self.horizontalLayout_point1.addWidget(self.point1_x)
        self.point1_y = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point1_y.sizePolicy().hasHeightForWidth())
        self.point1_y.setSizePolicy(sizePolicy)
        self.point1_y.setMinimumSize(QtCore.QSize(20, 20))
        self.point1_y.setObjectName("point1_y")
        self.horizontalLayout_point1.addWidget(self.point1_y)
        self.verticalLayout_points.addLayout(self.horizontalLayout_point1)
        self.horizontalLayout_point2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_point2.setObjectName("horizontalLayout_point2")
        self.point2_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point2_text.sizePolicy().hasHeightForWidth())
        self.point2_text.setSizePolicy(sizePolicy)
        self.point2_text.setObjectName("point2_text")
        self.horizontalLayout_point2.addWidget(self.point2_text)
        self.point2_x = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point2_x.sizePolicy().hasHeightForWidth())
        self.point2_x.setSizePolicy(sizePolicy)
        self.point2_x.setMinimumSize(QtCore.QSize(20, 20))
        self.point2_x.setObjectName("point2_x")
        self.horizontalLayout_point2.addWidget(self.point2_x)
        self.point2_y = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.point2_y.sizePolicy().hasHeightForWidth())
        self.point2_y.setSizePolicy(sizePolicy)
        self.point2_y.setMinimumSize(QtCore.QSize(20, 20))
        self.point2_y.setObjectName("point2_y")
        self.horizontalLayout_point2.addWidget(self.point2_y)
        self.verticalLayout_points.addLayout(self.horizontalLayout_point2)
        self.verticalLayout_sidebig.addLayout(self.verticalLayout_points)
        self.verticalLayout_buttons = QtWidgets.QVBoxLayout()
        self.verticalLayout_buttons.setObjectName("verticalLayout_buttons")
        self.horizontalLayout_cropping = QtWidgets.QHBoxLayout()
        self.horizontalLayout_cropping.setObjectName("horizontalLayout_cropping")
        self.cropButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cropButton.sizePolicy().hasHeightForWidth())
        self.cropButton.setSizePolicy(sizePolicy)
        self.cropButton.setObjectName("cropButton")
        self.horizontalLayout_cropping.addWidget(self.cropButton)
        self.undocropButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undocropButton.sizePolicy().hasHeightForWidth())
        self.undocropButton.setSizePolicy(sizePolicy)
        self.undocropButton.setObjectName("undocropButton")
        self.horizontalLayout_cropping.addWidget(self.undocropButton)
        self.verticalLayout_buttons.addLayout(self.horizontalLayout_cropping)
        self.horizontalLayout_filedialog = QtWidgets.QHBoxLayout()
        self.horizontalLayout_filedialog.setObjectName("horizontalLayout_filedialog")
        self.openButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout_filedialog.addWidget(self.openButton)
        self.saveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_filedialog.addWidget(self.saveButton)
        self.verticalLayout_buttons.addLayout(self.horizontalLayout_filedialog)
        self.verticalLayout_sidebig.addLayout(self.verticalLayout_buttons)
        self.main_horizontalLayout.addLayout(self.verticalLayout_sidebig)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 825, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.image_box.mousePressEvent = self.getPos

        self.retranslateUi(MainWindow)

        self.cropButton.clicked.connect(self.cropimage)
        self.undocropButton.clicked.connect(self.undo_crop)
        self.saveButton.clicked.connect(self.save_image)
        self.openButton.clicked.connect(self.open_image)
        self.pointselect1_button.clicked.connect(self.select_point1)
        self.pointselect2_button.clicked.connect(self.select_point2)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_point_text.setText(_translate("MainWindow", "Selected point x : 0 y : 0"))
        self.pointselect1_button.setText(_translate("MainWindow", "select to point 1"))
        self.pointselect2_button.setText(_translate("MainWindow", "select to poin 2"))
        self.point1_text.setText(_translate("MainWindow", "1.point : "))
        self.point2_text.setText(_translate("MainWindow", "2.point : "))
        self.cropButton.setText(_translate("MainWindow", "crop"))
        self.undocropButton.setText(_translate("MainWindow", "undo"))
        self.openButton.setText(_translate("MainWindow", "open"))
        self.saveButton.setText(_translate("MainWindow", "save"))
        self.point1_x.setText("0")
        self.point1_y.setText("0")
        self.point2_x.setText("0")
        self.point2_y.setText("0")

    def getPos(self, event):
        x = event.pos().x()
        y = event.pos().y()
        self.select_point_text.setText("Current point x : {0} y: {1}".format(x, y))

    def cropimage(self):
        try:
            if ((float(self.point1_x.text()) == 0) or (float(self.point1_y.text()) == 0)) and (
                    (float(self.point2_x.text()) == 0) or (float(self.point2_y.text()) == 0)):
                self.msg = QtWidgets.QMessageBox()
                self.msg.setText("Error")
                self.msg.setInformativeText('3 of the points cannot be zero')
                self.msg.setWindowTitle("Error")
                self.msg.exec_()
            else:
                to_cropsize = int(self.point1_x.text()), int(self.point1_y.text()), int(self.point2_x.text()), int(
                    self.point2_y.text())
                # r1 = QRect(100, 200, 11, 16)
                # r2 = QRect(QPoint(100, 200), QSize(11, 16))
                self.img_image = self.image_box.pixmap().toImage()
                pil_img_image = ImageQt.fromqimage(self.img_image)
                pil_img_image.show()
                self.image_before_cropped = self.image_box.pixmap()
                self.cropped_image = pil_img_image.crop(to_cropsize)
                temp_image = QtGui.QPixmap.fromImage(ImageQt.toqimage(self.cropped_image))
                self.image_box.setPixmap(temp_image)
                self.iscropped = True
        except Exception as errr:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setText("Error")
            self.msg.setInformativeText('Do not crop because this error {}'.format(errr))
            self.msg.setWindowTitle("Error")
            self.msg.exec_()

    def undo_crop(self):
        if self.iscropped:
            self.image_box.setPixmap(self.image_before_cropped)

    def select_point1(self):
        temp_point = self.select_point_text.text().split(" ")
        self.point1_x.setText(temp_point[4])
        self.point1_y.setText(temp_point[6])

    def select_point2(self):
        temp_point = self.select_point_text.text().split(" ")
        self.point2_x.setText(temp_point[4])
        self.point2_y.setText(temp_point[6])

    def open_image(self):
        image_name = QtWidgets.QFileDialog.getOpenFileName(self, "Open İmage", os.getenv("HOME"))
        with open(image_name[0], "r"):
            self.image_box.setPixmap(QtGui.QPixmap(image_name[0]))
            self.image_box.pixmap().scaledToWidth(64)
            self.image_box.pixmap().scaledToHeight(64)
            self.image_box.pixmap().scaled(64, 64, QtCore.Qt.KeepAspectRatio)
            self.image_box.pixmap().scaled(64,64)
            11büyük resimleri düzgün kesemiyor (yada hata veriyor)

    def save_image(self):
        image_name = QtWidgets.QFileDialog.getSaveFileName(self, "Save image", os.getenv("HOME"))
        self.image_box.pixmap().save(image_name)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.init_Ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
