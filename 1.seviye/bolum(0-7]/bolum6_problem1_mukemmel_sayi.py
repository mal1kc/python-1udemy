'''
mükemmel sayi denetleyici fonksiyonlarla
'''
def mukemmel_sayi(sayi):
    i = 1
    toplam = 0

    while i < sayi:
        if sayi % i == 0:
            toplam += i
        i += 1

    if toplam == sayi:
        return True
    else:
        return False

while True:
    sayi = input("Mükemmel sayı olup olmadığını denetlemek istediğiniz sayı nedir \n (çıkmak için 'q' tuşuna basınız) : ")
    if sayi == 'q':
        print("program kapatıldı, iyi günler")
        break
    elif mukemmel_sayi(int(sayi)):
        print("girdiğiniz {} sayısı mükemmel bir sayıdır .".format(sayi))
    else:
        print("girdiğiniz {} sayısı mükemmel bir sayı değildir .".format(sayi))