#bölüm 5 versiyonu
import random
print("""
-------------------------
kullanıcı girisi sürüm v1
-------------------------
""")
sonuclar = ["Kullanıcı Adı Hatalı", "Parola Hatalı"]
sys_kullanici_adi = "mal1c"

sys_parola = "sifre"

giris_hakki = 3
while True:
    kullanici_adi = input("Kullanıcı Adı : ")
    parola = input("Parola : ")
    if kullanici_adi != sys_kullanici_adi and parola == sys_parola:
        print("Kullanıcı Adı Hatalı .... ")
        giris_hakki -= 1
    elif kullanici_adi == sys_kullanici_adi and parola != sys_parola:
        print("Parola Hatalı .... ")
        giris_hakki -= 1
    elif kullanici_adi != sys_kullanici_adi and parola != sys_parola:
        print(random.choice(sonuclar))
        giris_hakki -= 1
    else:
        print("giriş başarılı .. ")
        break
    if giris_hakki == 0:
        print("giriş hakkınız tükenmiştir .. ")
        break

print("iyi günler dileriz ")