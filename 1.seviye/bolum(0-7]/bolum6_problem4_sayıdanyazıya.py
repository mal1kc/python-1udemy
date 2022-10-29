def sayidanyaziya(a):
    birlik = ["bir", "iki", "üç", "dört", "beş", "altı","yedi", "sekiz", "dokuz", ""]
    onluk = ["on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
    if len(str(a)) == 1:
        return birlik[a]
    elif len(str(a)) > 2:
        print("program şimdilik sadece 1 ve iki basamaklı sayılar ile çalışıyor")
    else:
        b = a // 10
        a = a % 10
        return (onluk[b - 1] + birlik[a - 1])

sayi = int(input("yazıya çevirmek istediğiniz sayıyı giriniz : "))
print("girdiğiniz sayı yazıla {} şeklinde ifade edilmektedir.".format(sayidanyaziya(sayi)))