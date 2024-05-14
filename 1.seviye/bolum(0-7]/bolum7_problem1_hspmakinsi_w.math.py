'''

math modulü ile hesap makinesi

'''

import math

print("""    0*********************************************************************************0
    0---------------------------------------------------------------------------------0

        # ilk olarak işlem seçiniz

        # ikinci olarak işlem yapmak istediğiniz değerleri sırasıyla giriniz

        işlem numaraları

        toplama = 1
        çıkarma = 2
        çarpma = 3
        bölme = 4
        mod işlemi için = 5
        üs almak için = 6
        sayının karekökünü almak için = 7 
        sayının logaritması için = 8
        dereceyi radyana çevirmek için = 9
        radyanı dereceye çevirmek için = 10
        sayının sinüs ünü bulmak için = 11
        sayının cos unu bulmak için = 12
        tanjantı bulmak için = 13
        cotanjantı bulmak için = 14

        çıkmak için q ya basın...

        #sin cos tan cot bunlarda radyan cisnsinden buluyor.

        #bir sayı ile yapılan işlemlerde(tekli işlemlerin yanında ' var)sadece ilk 
        girilen sayı için işlem yapılır( ikinci sayıya sıfır giriniz)

        #ilk girilen sayının ikinciye işlemini yapar
        (örneğin ilk girilen sayının ikinciye modu alınır)

    0---------------------------------------------------------------------------------0
    0*********************************************************************************0""")

while True:

    i = str(input("yapmak istediğiniz işlemin numarası : "))

    if i == 'q':
        print("program kapatılıyor ..")
        break
    else:

        i = int(i)

        if i > 0 and 14 >= i:

            a = int(input("birinci sayı : "))

            b = int(input("ikinci sayı : "))

            if i == 1:
                print("giridiğiniz {} sayısı ile {} sayısı toplamı = {} ".format(a, b, a + b))
            elif i == 2:
                print("giridiğiniz {} sayısından {} sayısının çıkarımı sonucu = {} ".format(a, b, a - b))
            elif i == 3:
                print("giridiğiniz {} sayısı ile {} sayısı çarpımı = {} ".format(a, b, a * b))
            elif i == 4:
                print("giridiğiniz {} sayısının {} sayısına bölümü  sonucu = {} ".format(a, b, a / b))
            elif i == 5:
                print("giridiğiniz {} mod {}  işleminin sonucu = {} ".format(a, b, a % b))
            elif i == 6:
                print("giridiğiniz {} üstü {}  işleminin sonucu = {} ".format(a, b, pow(a, b)))
            elif i == 7:
                print("giridiğiniz {} sayısının karekök işleminin sonucu = {} ".format(a, math.sqrt(a)))
            elif i == 8:
                print("giridiğiniz {} log {}  işleminin sonucu = {} ".format(a, b, math.log(a, b)))
            elif i == 9:
                print("giridiğiniz {} radyana çevrilmesi işleminin sonucu = {} ".format(a, b, math.radians(a)))
            elif i == 10:
                print("giridiğiniz {} dereceye çevrilmesi  işleminin sonucu = {} ".format(a, math.degrees(a)))
            elif i == 11:
                print("giridiğiniz {} sayının sinüs işleminin sonucu = {} ".format(a, math.sin(a)))
            elif i == 12:
                print("giridiğiniz {} sayının cosinusu sonucu = {} ".format(a, math.cos(a)))
            elif i == 13:
                print("giridiğiniz {} sayının tanjantı sonucu = {} ".format(a, math.tan(a)))
            elif i == 14:
                print("giridiğiniz {} sayının cotanjantı sonucu = {} ".format(a, (math.tan(a) / 1)))
        else:
            print("geçersiz işlem numarası")

