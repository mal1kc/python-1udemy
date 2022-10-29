#
# Proje 2
#
# Elinizde 5 kişinin maillerinin ve isimlerinin bulunduğu bir dosya olsun. Bu dosyayı okuyarak, her bir kişiye
# isimleriyle beraber mail göndermeye çalışın. Dosya formatı şu şekilde olacak.
#
#                        Mustafa Murat Coşkun,coskun.m.murat@gmail.com
#                                        //
#                                        //
#                                        //
#                                        //
#
# https://myaccount.google.com/lesssecureapps

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'mail_adresi@gmail.com'
PASSWORD = 'mail_adresi_şifresi 


def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as adresses:
        for a_contact in adresses:
            emails.append(a_contact.split(",")[0])
            names.append(a_contact.split(",")[1])
    return names, emails


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return template_file_content


def main():
    names, emails = get_contacts('maill_adresses.txt')  # read contacts
    message_template = read_template('mail_content.txt')
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message
        message = message_template.replace("PERSON_NAME", name.strip("\n"))
        # print(message)
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Sending mail to all"
        msg.attach(MIMEText(message, 'plain'))
        s.send_message(msg)
        del msg
    s.quit()


if __name__ == '__main__':
    main()
# with open("mailler.txt","r+",encoding="utf-8") as file:
#     icerik = file.readlines()
#     gerekliler = set()
#     file.seek(0)
#     for i in icerik:
#         i = i.strip("\n")
#         if i.endswith(r"gmail.com"):
#             gerekliler.add(i)
#
#     for j in gerekliler:
#         file.write(j + "\n")
#         print(j)
#     file.truncate()
