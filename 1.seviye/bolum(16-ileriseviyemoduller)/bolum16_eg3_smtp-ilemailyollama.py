import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# https://myaccount.google.com/lesssecureapps

mesaj = MIMEMultipart()

mesaj["From"] = "from@gmail.com" # yollayan mail adresi
mesaj["To"] = "to@gmail.com" # hedef mail adresi
mesaj["Subject"] = "Smtp mödülü deneme"

yazi = """

Smtp mödülünü deniyorum

Malik

"""

mesaj_govdesi = MIMEText(yazi, "plaind")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(mesaj["From"], a"MAİL ŞİFRESI")
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("mail başarıyla gönderildi")
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu")
