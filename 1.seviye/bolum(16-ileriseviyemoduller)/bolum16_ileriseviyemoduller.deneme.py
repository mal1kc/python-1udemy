# from datetime import datetime
# import locale
#
# locale.setlocale(locale.LC_ALL, "")
# su_an = datetime.now()
# print(datetime.timestamp(su_an))
# print(su_an)
# print(datetime.strftime(su_an, "%Y %B %A"))
# import os
#
# # print(datetime.fromtimestamp(os.stat("test.txt").st_mtime))
# # os.rename("test.txt", "test.py")
#
# # os.mkdir("denem1")
# # os.rmdir("denem1")
# # print(os.getcwd())
# # os.chdir("C:/Users/malik kokcan/Desktop")
# # print(os.getcwd())
# # print(os.listdir())
#
# for klasor_yolu, klasör_isimleri, dosya_isimleri in os.walk("D:/malik kokcan"):
#     # print("Current Path", klasor_yolu)
#     # print("Directories", klasör_isimleri)
#     # print("Dosyalar", dosya_isimleri)
#     # print("**********************************")
#     for i in dosya_isimleri:
#         if i.endswith(".txt"):
#             print(i)

# import sys
# print(dir(sys))
# sys.stderr.write("hata veriyorum alıyor musun\n")
# sys.stderr.flush()
# sys.stdout.write("normal mesaj\n")
# sys.argv terminalden çalıştıırılınca girilen argumanları verir
# for i in sys.argv:
#     print(i)
#
# def kok_bulma(a, b, c):
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print("reel kök yok")
#     else:
#         x1 = (-b - delta ** 0.5) / 2 * a
#         x2 = (-b + delta ** 0.5) / 2 * a
#         return x1, x2
#
# if len(sys.argv) == 4:
#     print("kökö bulma : ", kok_bulma((int(sys.argv[1])), int(sys.argv[2]), int(sys.argv[3])))
# else:
#     sys.stderr.write("eksik parametre girdiniz")
#     sys.stderr.flush()
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://genius.com/Farazi-v-kayra-bir-gunluk-oldurun-beni-lyrics"
# response = requests.get(url)
# print(response)
# html_icerigi = response.content
# soup = BeautifulSoup(html_icerigi,"html.parser")
# print(soup.find_all("div",{"class":"lyrics"}))

# yukarısı ilk öğrenim notlarım












