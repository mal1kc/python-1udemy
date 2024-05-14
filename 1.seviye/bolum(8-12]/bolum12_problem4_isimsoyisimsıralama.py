#
# Problem 4
#
# Elinizde 2 tane liste bulunsun. Bu listelerden isim ve soyisimleri birleştirerek , ekrana isim ve soyisimleri
# isimlere göre sıralı bir şekilde yazdırmaya çalışın.
#
#         isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
#
#         soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
#
isimler = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve", "Erdal"]
soyisimler = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat", "İtoğlu"]
isimlersirali = dict()

for i, j in zip(isimler, soyisimler):
    isimlersirali[i] = j
for i in sorted(isimlersirali):
    print("{} : {}".format(i, isimlersirali[i]))
