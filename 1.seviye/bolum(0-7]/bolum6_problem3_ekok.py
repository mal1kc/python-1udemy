'''

ekok bulan program

'''

def ekok(a,b):
    enb = a
    i = 2
    ekok = 1
    if b > a:
        enb = b
    while a != 1 or b != 1:
        if (a % i == 0) and (b % i == 0 ):
            ekok *= i

            a //= i
            b //= i
        elif (a % i == 0) and (b % i != 0):
            ekok *= i

            a //= i
        elif (a % i != 0) and (b % i == 0):
            ekok *= i

            b //= i
        else:
            i += 1
    return ekok

sayi1 = int(input("ekok işlemi için birinci sayıyı giriniz : "))
sayi2 = int(input("ekok işlemi için ikinci sayıyı giriniz : "))

print("ekok işlemi sonucu : {} ".format(ekok(sayi1,sayi2)))