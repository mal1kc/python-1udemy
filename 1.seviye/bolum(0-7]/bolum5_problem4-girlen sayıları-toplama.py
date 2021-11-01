print("""
-------------------
q ya basana kadar girilen sayıları toplayan program
-------------------
""")

toplam = 0
while True:
    sayi = input("Sayı giriniz (Çıkmak için 'q' tuşuna basın) : ")
    if sayi == "q":
        print("Toplam : ", toplam)
        break
    sayi = int(sayi)
    toplam += sayi