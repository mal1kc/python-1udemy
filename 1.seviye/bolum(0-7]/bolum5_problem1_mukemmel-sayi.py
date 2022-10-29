# bolum5-problem1
print("""----------------------------------------------------------------------------------------------
Mukemmel Sayı Bulucu
(Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir)
----------------------------------------------------------------------------------------------""")


while True:
    girdi = input("Sayi (Cikmak için 'q' tuşuna basınız) : ")
    if girdi == "q":
        print("çıkış yapılıyor ..")
        break
    sayi = int(girdi)

    i = 1
    toplam = 0

    while i < sayi:
        if sayi % i == 0:
            toplam += i
        i += 1

    if toplam == sayi:
        print("{} mükemmel bir sayidir . ".format(sayi))
    else:
        print(sayi, " mükemmel bir sayi değildir . ")
