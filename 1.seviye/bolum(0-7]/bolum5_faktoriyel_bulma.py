print("""-------------------
Faktoriyel Bulma Programı

Programdan çıkmak için 'q' ya basın.
-------------------""")

while True:

    sayi = input("Faktoriyeli bulunacak sayı (çıkmak için 'q') : ")
    if sayi == "q":
        print("programdan sonlandırılıyor")
        break
    else:
        sayi = int(sayi)
        for i in range(2, sayi):
            sayi *= i
        print("Faktöriyel işlemi sonucu : ", sayi)