# Proje 1
#
# Bilgisayarınızdaki tüm mp4,txt ve pdf dosyalarını os modülüyle arayın ve bunların nerede bulunduklarını ve
# isimlerini ayrı ayrı "pdf_dosyalari.txt","mp4_dosyaları.txt","txt_dosyaları.txt" adlı dosyalara kaydedin.
import os

mp4f = open("mp4.txt", "w", encoding="utf-8")
txtf = open("txt.txt", "w", encoding="utf-8")
pdff = open("pdf.txt", "w", encoding="utf-8")
aranicak = os.walk("D:/jdownloader")

for klasor_yolu, klasor_ismi, dosya_ismi in aranicak:
    for dosya in dosya_ismi:
        yol = klasor_yolu
        if dosya.endswith("txt"):
            txtf.write("dosya yolu " + yol + ", dosya adı" + dosya + "\n")
        elif dosya.endswith("mp4"):
            mp4f.write("dosya yolu " + yol + ", dosya adı" + dosya + "\n")
        elif dosya.endswith("pdf"):
            pdff.write("dosya yolu " + yol + ", dosya adı" + dosya + "\n")
mp4f.close()
txtf.close()
pdff.close()
with open("mp4.txt", "r", encoding="utf-8") as mp4f:
    print("{} tane mp4 dosyası bulundu".format(len(mp4f.readlines())))
with open("txt.txt", "r", encoding="utf-8") as txtf:
    print("{} tane txt dosyası bulundu".format(len(txtf.readlines())))
with open("pdf.txt", "r", encoding="utf-8") as pdff:
    print("{} tane pdf dosyası bulundu".format(len(pdff.readlines())))
