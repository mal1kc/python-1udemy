import sys
from PyQt5 import QtCore, QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class UiMainWindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("MainWindow")
        mainwindow.setWindowModality(QtCore.Qt.WindowModal)
        mainwindow.resize(805, 602)
        mainwindow.setMinimumSize(QtCore.QSize(805, 602))
        mainwindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 571))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.emails_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.emails_text.setObjectName("emails_text")
        self.verticalLayout.addWidget(self.emails_text)
        self.emails = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.emails.setObjectName("emails")
        self.verticalLayout.addWidget(self.emails)
        self.mail_content_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.mail_content_text.setObjectName("mail_content_text")
        self.verticalLayout.addWidget(self.mail_content_text)
        self.mail_content = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.mail_content.setObjectName("mail_content")
        self.verticalLayout.addWidget(self.mail_content)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setText("SMTP MAİL SERVER")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.smtp_adress_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.smtp_adress_text.setObjectName("smtp_adress_text")
        self.horizontalLayout_4.addWidget(self.smtp_adress_text)
        self.smtp_adress = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.smtp_adress.setObjectName("smtp_adress")
        self.horizontalLayout_4.addWidget(self.smtp_adress)
        self.smtp_port_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.smtp_port_text.setObjectName("smtp_port_text")
        self.horizontalLayout_4.addWidget(self.smtp_port_text)
        self.smtp_adress_port = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.smtp_adress_port.setObjectName("smtp_adress_port")
        self.horizontalLayout_4.addWidget(self.smtp_adress_port)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.username_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.username_text.setObjectName("username_text")
        self.horizontalLayout_3.addWidget(self.username_text)
        self.username = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.username.setObjectName("username")
        self.horizontalLayout_3.addWidget(self.username)
        self.password_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.password_text.setObjectName("password_text")
        self.horizontalLayout_3.addWidget(self.password_text)
        self.password = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.sendmails_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sendmails_button.setObjectName("sendmails_button")
        self.verticalLayout_2.addWidget(self.sendmails_button)
        self.output_label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.output_label1.setText("")
        self.output_label1.setObjectName("output_label1")
        self.verticalLayout_2.addWidget(self.output_label1)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        self.sendmails_button.clicked.connect(self.send_mails)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "smtp mail sender"))
        self.emails_text.setText(_translate("MainWindow", "Sending Emails , Names"))
        self.emails.setPlainText(_translate("MainWindow", "mail@mail.com , name \\ min 2 mails"
                                                          "mail2@mail.com, mail2person"))
        self.mail_content_text.setText(_translate("MainWindow", "Mail Content"))
        self.mail_content.setPlainText(_translate("MainWindow", "PERSON_NAME, blablablablalbla"))
        self.smtp_adress_text.setText(_translate("MainWindow", "smtp adress"))
        self.smtp_adress.setText(_translate("MainWindow", "smtp.gmail.com"))
        self.smtp_port_text.setText(_translate("MainWindow", "port"))
        self.smtp_adress_port.setText(_translate("MainWindow", "587"))
        self.username_text.setText(_translate("MainWindow", "Your mail adress"))
        self.username.setText(_translate("MainWindow", "mail@mail.com"))
        self.password_text.setText(_translate("MainWindow", "Your Password"))
        self.password.setText(_translate("MainWindow", "sifre"))
        self.sendmails_button.setText(_translate("MainWindow", "send mails"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<h1 align=\"center\" style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ff0000;\"><span style=\" font-size:xx-large; font-weight:600; color:#ffffff; background-color:#ff0000;\">!!!Warning!!!</span></h1>\n"
                                         "<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'verdana\'; font-size:20px;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20px;\">if you are use gmail accout you turn on lessecure app setting in </span><a href=\"https://myaccount.google.com/lesssecureapps\"><span style=\" font-size:20px; text-decoration: underline; color:#0000ff;\">myaccount.google.com/lesssecureapps</span></a></li>\n"
                                         "<li style=\" font-family:\'verdana\'; font-size:20px;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20px;\">if you are add emails like that </span></li></ul>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; background-color:#ff0000;\"><span style=\" font-family:\'verdana\'; font-size:20px; background-color:#ff0000;\">name@email.com , name</span></p>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-family:\'verdana\'; font-size:20px;\">mail send like ;</span></p>\n"
                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; background-color:#ff0000;\"><span style=\" font-family:\'verdana\'; font-size:20px; background-color:#ff0000;\">_NAME,other mail content</span> </p></body></html>"))

    def get_contacts(self):
        names = []
        emails = []
        adresses = self.emails.toPlainText().split("\n")
        for a_contact in adresses:
            emails.append(a_contact.split(",")[0])
            names.append(a_contact.split(",")[1])
        return names, emails

    def send_mails(self):
        try:
            names, emails = self.get_contacts()  # read contacts
            message_template = self.mail_content.toPlainText()
            s = smtplib.SMTP(host=self.smtp_adress.text(), port=int(self.smtp_adress_port.text()))
            s.starttls()
            my_address = self.username.text()
            password = self.password.text()
            s.login(my_address, password)
            for name, email in zip(names, emails):
                msg = MIMEMultipart()  # create a message
                message = message_template.replace("_NAME", name.strip("\n"))
                print(message)
                msg['From'] = my_address
                msg['To'] = email
                msg['Subject'] = "Sending mail to all"
                msg.attach(MIMEText(message, 'plain'))
                s.send_message(msg)
                del msg
            self.output_label1.setStyleSheet("background-color: green;")
            self.output_label1.setText("mails succesfuly send")
        except Exception as error:
            self.output_label1.setStyleSheet("background-color: red;")
            self.output_label1.setText("mails not sent {}".format(error))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
