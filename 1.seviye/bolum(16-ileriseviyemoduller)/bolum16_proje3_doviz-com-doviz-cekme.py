#
# Proje 3
#
# https://www.doviz.com/ sitesinden anlık olarak doların,euronun,altının ve borsanın değerlerini öğrenin ve bunları
# kullanarak bir proje geliştirmeye çalışın.
#
# Not: Bu projeyi, requests ve beautifulsoup kullanarak geliştirin.
import datetime
from time import sleep
import requests
from bs4 import BeautifulSoup


def dovizleri_cek():
    url = "https://www.doviz.com"
    response = requests.get(url)
    html_icerigi = response.content
    soup = BeautifulSoup(html_icerigi, "html.parser")
    gram_altin = float(soup.find("span", {"data-socket-key": "gram-altin"}).text.replace(",", "."))
    usd = float(soup.find("span", {"data-socket-key": "USD"}).text.replace(",", "."))
    eur = float(soup.find("span", {"data-socket-key": "EUR"}).text.replace(",", "."))
    sterlin = float(soup.find("span", {"data-socket-key": "GBP"}).text.replace(",", "."))
    bitcoin = soup.find("span", {"data-socket-key": "bitcoin"}).text[1:]
    return gram_altin, usd, eur, sterlin, bitcoin


print("gram altin : {0}₺\nUSD : {1}₺\nEUR : {2}₺\nSterlin : {3}₺\nBitcoin : {4}\n".format(dovizleri_cek()[0],
                                                                                          dovizleri_cek()[1],
                                                                                          dovizleri_cek()[2],
                                                                                          dovizleri_cek()[3],
                                                                                          dovizleri_cek()[4]))

with open("15lı.doviz.comverisi.txt", "r+", encoding="utf-8") as f:
    giris = datetime.datetime.now()
    while (datetime.datetime.now() - giris).seconds < (2 * 60):
        f.write(
            "zaman: {0}\t--\tGram-altin: {1:,.3f}\t--\ttUSD : {2:,.3f}\t--\tEUR : {3:,.3f}\t--\tSTERLİN : {4:,.3f}\t--\tBTC : {5}\n".format(
                datetime.datetime.now(), dovizleri_cek()[0], dovizleri_cek()[1], dovizleri_cek()[2], dovizleri_cek()[3],
                dovizleri_cek()[4]))
        sonraki = datetime.datetime.now()
        print("geçen süre : {:.2f} dk".format((sonraki - giris).seconds / 60), end="\t")
        print("kalan süre : {:.2f} dk\n".format((2 * 60 - (sonraki - giris).seconds) / 60), end="")
        sleep(30)
    print("\nişlem tamamlandı iyi günler\n")
