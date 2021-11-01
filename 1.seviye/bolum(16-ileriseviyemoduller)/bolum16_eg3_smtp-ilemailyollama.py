import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# https://myaccount.google.com/lesssecureapps

mesaj = MIMEMultipart()

mesaj["From"] = "kixxayy@gmail.com"
mesaj["To"] = "kixxayy@gmail.com"
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
    mail.login("kixxayy@gmail.com", "kixxayyN@b3r;(l*N)")
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("mail başarıyla gönderildi")
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu")
