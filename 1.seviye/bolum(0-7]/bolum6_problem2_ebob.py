'''

2 sayi arasında EBOB bulucu fonksiyon ve kullanım örneği

'''

def ebob(a,b):
    i = 1
    ebob = 1
    while (i <= a and i <= b):
        if (not (a % i) and not (b % i)):
            ebob = i
        i += 1
    return ebob

sayi1 = int(input("ebob işlemi için birinci sayıyı giriniz : "))
sayi2 = int(input("ebob işlemi için ikinci sayıyı giriniz : "))
sonuc = ebob(sayi1,sayi2)
if (sonuc == 1) :
    print("en büyük ortak bölenleri yoktur (1 dir) ")
print("ebob işlemi sonucu : {} ".format(sonuc))