#
# Problem 3
#
# Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir satırını
# okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.
#
#                     coskun.m.murat@gmail.com
#                     example@xyz.com
#                     mustafa.com
#                     mustafa@gmail
#                     kerim@yahoo.com
#
#                            //
#                            //
#                            //
#
#
# İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz.
# --------------------- bir hata yapıp sadece mail olanları dosyaya geri yazdırdım -----------------------------------
with open("bolum12_problem3_mailler.txt", "r", encoding="utf-8") as file:
    icerik = file.readlines()
    mailler = set()
    for i in icerik:
        i = i.strip(" ")
        i = i.strip("\n")
        if i.find("@") != -1:
            mailler.add(i)

with open("bolum12_problem3_mailler.txt", "w", encoding="utf-8") as file:
    for i in mailler:
        file.write(i + "\n")
