import requests
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLineEdit, \
    QComboBox, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PyQt5 import QtCore, QtGui


class UiForm(object):
    def setupUi(self, form):
        form.setObjectName("Form")
        form.resize(859, 510)
        self.horizontalGroupBox = QGroupBox(form)
        self.horizontalGroupBox.setGeometry(QtCore.QRect(0, 0, 851, 501))
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout = QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.all_currencies = QPlainTextEdit(self.horizontalGroupBox)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.all_currencies.setFont(font)
        self.all_currencies.setObjectName("all_currencies")
        self.verticalLayout.addWidget(self.all_currencies)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_amount = QLineEdit(self.horizontalGroupBox)
        self.input_amount.setFont(font)
        self.input_amount.setObjectName("input_amount")
        self.verticalLayout_2.addWidget(self.input_amount)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.currency_1 = QLabel(self.horizontalGroupBox)
        self.currency_1.setFont(font)
        self.currency_1.setObjectName("currency_1")
        self.horizontalLayout_3.addWidget(self.currency_1)
        self.currency_select1 = QComboBox(self.horizontalGroupBox)

        self.currency_select1.setFont(font)
        self.currency_select1.setObjectName("currency_select1")
        self.horizontalLayout_3.addWidget(self.currency_select1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.currency_2 = QLabel(self.horizontalGroupBox)
        self.currency_2.setFont(font)
        self.currency_2.setObjectName("currency_2")
        self.horizontalLayout_4.addWidget(self.currency_2)
        self.currency_select2 = QComboBox(self.horizontalGroupBox)
        self.currency_select2.setFont(font)
        self.currency_select2.setObjectName("currency_select2")
        self.horizontalLayout_4.addWidget(self.currency_select2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.output_amount = QLineEdit(self.horizontalGroupBox)
        self.output_amount.setFont(font)
        self.output_amount.setObjectName("output_amount")
        self.verticalLayout_2.addWidget(self.output_amount)
        self.calculate = QPushButton(self.horizontalGroupBox)
        self.calculate.setFont(font)
        self.calculate.setObjectName("calculate")
        self.verticalLayout_2.addWidget(self.calculate)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.reflesh_button = QPushButton(self.horizontalGroupBox)
        font.setWeight(75)
        self.reflesh_button.setFont(font)
        self.reflesh_button.setObjectName("reflesh_button")
        self.horizontalLayout_2.addWidget(self.reflesh_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(form)
        form.setWindowTitle("currency calculator")
        self.reflesh_button.clicked.connect(self.pull_data)
        self.calculate.clicked.connect(self.calculate_currency)

        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        self.currency_1.setText(_translate("Form", "Curency"))
        self.currency_2.setText(_translate("Form", "To Curency"))
        self.calculate.setText(_translate("Form", "calculate"))
        self.reflesh_button.setText(_translate("Form", "reflesh data"))

    def pull_data(self):
        url = "http://data.fixer.io/api/latest?access_key=***REMOVED***"
        response = requests.get(url)
        self.json_data = response.json()
        for i, j in self.json_data["rates"].items():
            self.all_currencies.setPlainText(self.all_currencies.toPlainText() + i + "\t" + str(j) + "= 1.0 €\n")
            self.all_currencies.setReadOnly(True)
            self.currency_select1.addItem(i)
            self.currency_select2.addItem(i)

    def calculate_currency(self):
        curency_1 = self.currency_select1.currentText()
        curency_2 = self.currency_select2.currentText()
        input_amount = float(self.input_amount.text())
        if self.json_data["rates"][curency_1] > self.json_data["rates"][curency_2]:
            result = (self.json_data["rates"][curency_1] / self.json_data["rates"][curency_2]) * input_amount
            self.output_amount.setText("{0:,.2f} {1} = {3:,.2f} {2}".format(input_amount, curency_2, curency_1, result))
        else:
            result = (self.json_data["rates"][curency_2] / self.json_data["rates"][curency_1]) * input_amount
            self.output_amount.setText("{0:,.2f} {1} = {3:,.2f} {2}".format(input_amount, curency_1, curency_2, result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = UiForm()
    ui.setupUi(Form)
    Form.show()
    ui.pull_data()
    sys.exit(app.exec_())
