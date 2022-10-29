import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup


def get_image_from_url(image_url):
    import urllib
    import os
    search = os.walk("\\temp")
    searched = list()
    for i, j, f in search:
        for fi in f:
            searched.append(fi)
    filename = image_url.split("/")[-1]
    i = len(searched)
    if filename in searched:
        return filename
    else:
        new_image_filename = "temp_" + str(i) + ".jpg"
        os.chdir("temp")
        downloaded_filename = urllib.request.urlretrieve(image_url, new_image_filename)
        os.chdir("..")
        return "temp\\" + downloaded_filename[0]


class Ui_Form(object):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.movie_widgets = dict()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(663, 378)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.min_rating_label = QtWidgets.QLabel(Form)
        self.min_rating_label.setAlignment(QtCore.Qt.AlignCenter)
        self.min_rating_label.setWordWrap(True)
        self.min_rating_label.setObjectName("min_rating_label")
        self.horizontalLayout.addWidget(self.min_rating_label)
        self.min_rating_star = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_rating_star.sizePolicy().hasHeightForWidth())
        self.min_rating_star.setSizePolicy(sizePolicy)
        self.min_rating_star.setText("")
        self.min_rating_star.setPixmap(QtGui.QPixmap("imdb_star.png"))
        self.min_rating_star.setObjectName("min_rating_star")
        self.horizontalLayout.addWidget(self.min_rating_star)
        self.min_rating = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min_rating.sizePolicy().hasHeightForWidth())
        self.min_rating.setSizePolicy(sizePolicy)
        self.min_rating.setObjectName("min_rating")
        self.horizontalLayout.addWidget(self.min_rating)
        self.get_movies = QtWidgets.QPushButton(Form)
        self.get_movies.setObjectName("get_movies")
        self.horizontalLayout.addWidget(self.get_movies)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 634, 708))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 1)

        self.retranslateUi(Form)

        self.get_movies.clicked.connect(lambda: self.get_movies_(float(self.min_rating.text())))
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "imdb top 250"))
        self.min_rating_label.setText(_translate("Form", "min rating"))
        self.min_rating.setText(_translate("Form", "7.0"))
        self.get_movies.setText(_translate("Form", "get movies"))

    def get_movies_(self, min_rating=7.0):
        url = "https://www.imdb.com/chart/top"
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content, "html.parser")

        posters_content = soup.find_all("img", src=True)
        posters_links = list()
        for i in posters_content:
            posters_links.append(i['src'])

        titles = soup.find_all("td", {"class": "titleColumn"})
        ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})

        for title, rating, poster_url, number in zip(titles, ratings, posters_links, range(len(titles))):
            try:
                if float(rating.text) >= min_rating:
                    self.movie_widgets[number] = {}
                    self.temp_item = "movie_item_" + str(number)
                    self.movie_widgets[number]["QHBOX"] = QtWidgets.QHBoxLayout()
                    self.movie_widgets[number]["QHBOX"].setObjectName(self.temp_item)
                    self.movie_widgets[number]["QHBOX"].setContentsMargins(5, 5, 5, 5)

                    self.temp_movie_poster = "movie_poster_" + str(number)
                    self.temp_movie_poster_image = QtGui.QImage(get_image_from_url(poster_url))
                    self.movie_widgets[number]["POSTER"] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                    self.movie_widgets[number]["POSTER"].setObjectName(self.temp_movie_poster)
                    self.movie_widgets[number]["POSTER"].setPixmap(QtGui.QPixmap(get_image_from_url(poster_url)))

                    self.movie_widgets[number]["QHBOX"].addWidget(self.movie_widgets[number]["POSTER"])

                    self.temp_movie_name = "movie_name_" + str(number)
                    self.temp_movie_text = title.text.strip()
                    self.temp_movie_text = title.text.replace("\n", "")
                    self.movie_widgets[number]["NAME"] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                    self.movie_widgets[number]["NAME"].setObjectName(self.temp_movie_name)
                    self.movie_widgets[number]["NAME"].setText(self.temp_movie_text)
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                    sizePolicy.setHorizontalStretch(60)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(self.movie_widgets[number]["NAME"].sizePolicy().hasHeightForWidth())

                    self.movie_widgets[number]["NAME"].setSizePolicy(sizePolicy)
                    self.movie_widgets[number]["QHBOX"].addWidget(self.movie_widgets[number]["NAME"])

                    self.temp_star_name = "star_name" + str(number)
                    self.movie_widgets[number]["STAR"] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                    self.movie_widgets[number]["STAR"].setText("")
                    self.movie_widgets[number]["STAR"].setPixmap(QtGui.QPixmap("imdb_star.png"))
                    self.movie_widgets[number]["STAR"].setObjectName(self.temp_star_name)
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(self.movie_widgets[number]["STAR"].sizePolicy().hasHeightForWidth())

                    self.movie_widgets[number]["STAR"].setSizePolicy(sizePolicy)
                    self.movie_widgets[number]["QHBOX"].addWidget(self.movie_widgets[number]["STAR"])

                    self.temp_rating_name = "rating_name_" + str(number)
                    self.temp_rating_text = rating.text
                    self.movie_widgets[number]["RATING"] = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                    self.movie_widgets[number]["RATING"].setObjectName(self.temp_rating_name)
                    self.movie_widgets[number]["RATING"].setText(self.temp_rating_text)
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(self.movie_widgets[number]["RATING"].sizePolicy().hasHeightForWidth())

                    self.movie_widgets[number]["RATING"].setSizePolicy(sizePolicy)
                    self.movie_widgets[number]["QHBOX"].addWidget(self.movie_widgets[number]["RATING"])

                    self.gridLayout_2.addLayout(self.movie_widgets[number]["QHBOX"])
                    print(self.temp_movie_name + self.temp_movie_text)

            except Exception as errr:
                self.msg = QtWidgets.QMessageBox()
                self.msg.setText("Error")
                self.msg.setInformativeText('Do not getmovies because this error {}'.format(errr))
                self.msg.setWindowTitle("Error")
                self.msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.get_movies_(7.0)
    Form.show()
    sys.exit(app.exec_())
