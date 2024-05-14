#
# Proje 2
#
# "futbolcular.txt" şeklinde bir dosya oluşturun ve içine Galatasaray,Fenerbahçe ve Beşiktaşta oynayan futbolcuları
# rastgele yerleştirin. Bu dosyadan herbir takımın futbolcularını ayırarak "gs.txt" , "fb.txt", "bjk.txt" şeklinde
# 3 farklı dosyaya yazın.
#
# "futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.
#
#                 Fernando Muslera,Galatasaray
#                 Atiba Hutchinson,Beşiktaş
#                 Simon Kjaer,Fenerbahçe
#                            //
#                            //
#                            //
#                            //
#                            //

import random


def yerlestir(oyuncu, takim=1, takimlar=None):
    if takimlar is None:
        takimlar = ["bolum10_proje2_gs.txt", "bolum10_proje2_fb.txt", "bolum10_proje2_bjk.txt"]
    with open(takimlar[takim], "r+", encoding="utf-8") as file:
        takim_oyunculari = file.readlines()
        if 10 < len(takim_oyunculari):
            yerlestir(oyuncu, random.randint(0, 2))

        else:
            file.write(oyuncu + "\n")


takimlarim = ["bolum10_proje2_gs.txt", "bolum10_proje2_fb.txt", "bolum10_proje2_bjk.txt"]

with open("bolum10_proje2_oyuncular.txt", "r", encoding="utf-8") as file1:
    oyuncular = file1.readlines()
    for i in oyuncular:
        i = i[:-1]
        yerlestir(i, random.randint(0, 2), takimlarim)

