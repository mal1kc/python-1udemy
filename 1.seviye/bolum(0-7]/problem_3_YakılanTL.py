print("Yak.TL ilk sürüm")
veri0 = int(input("Yapılan yolu giriniz(Kilometre) = "))
veri1 = float(input("km başına yakılan yakıt = "))
veri2 = float(input("Yakıtın birim değeri = "))
veriler = [veri0,veri1,veri2]
print("girilen veriler okunuyor ve işleniyor ... \n lütfen bekleyiniz.. .")
print("Ödemeniz gereken tutar : {} TL".format(veriler[0]*veriler[1]*veriler[2]))
print("İşlem tamamlandı.")
