"""

Asal sayı bulma

"""
def asal_mi(sayi):
    if (sayi == 1 ):
        return  False
    elif (sayi == 2):
        return  True
    else:
        for i in  range(2,sayi):
            if (sayi % i == 0 ):
                return False
        return True

sayi = int(input("Asallığını kontrol etmek istediğiniz bir sayı giriniz : "))
if asal_mi(sayi):
    print("giridiğiniz {} sayısı asaldır ".format(sayi))
else:
    print("giridiğiniz {} sayısı asal değildir ".format(sayi))