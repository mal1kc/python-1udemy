from urllib.request import urlretrieve

import PIL.Image
import requests
from bs4 import BeautifulSoup
from PIL import Image


def get_image_from_url(image_url):
    import urllib
    import os
    search = os.walk("\\temp")
    searched = list()
    for i, j, f in search:
        for fi in f:
            searched.append(fi)
    print(searched)
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


url = "https://www.imdb.com/chart/top"
response = requests.get(url)
html_icerigi = response.content
soup = BeautifulSoup(html_icerigi, "html.parser")

a = 7.0


posters_content = soup.find_all("img", src=True)
posters_links = list()
for i in posters_content:
    posters_links.append(i['src'])
basliklar = soup.find_all("td", {"class": "titleColumn"})
puanlar = soup.find_all("td", {"class": "ratingColumn imdbRating"})
for baslik, puan, poster in zip(basliklar, puanlar, posters_links):
    baslik = baslik.text
    poster_img = Image.open(get_image_from_url(poster))
    poster_img.show()
    puan = puan.text
    baslik = baslik.strip()
    baslik = baslik.replace("\n", "")
    puan = puan.strip()
    puan = puan.replace("\n", "")
    if float(puan) > a:
        print("{} puanı {}".format(baslik, puan))

# Proje 4
#
# İleri Seviye Modüller bölümünde yaptığımız Imdb film verileri işlemini arayüz halinde geliştirmeye çalışın.
