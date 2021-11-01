print("""0*********************************************************************************0
        
      # ilk olarak işlem seçiniz
      
      # ikinci olarak işlem yapmak istediğiniz değerleri giriniz
      
      1.İşlem Toplama
     
      2.İşlem Çıkarma
     
      3.İşlem Çarpma
      
      4.İşlem Bölme
      
      5.Modunu hesaplama
      #ilk girilen sayının ikinciye modu
      
0*********************************************************************************0""")
i = int(input("yapmak istediğiniz işlemin numarası : "))

if i > 0 and 5 >= i :

    a = int(input("birinci sayı : "))

    b = int(input("ikinci sayı : "))

    if i == 1:
        print("giridiğiniz {} sayısı ile {} sayısı toplamı = {} ".format(a, b, a + b))
    if i == 2:
        print("giridiğiniz {} sayısından {} sayısının çıkarımı sonucu = {} ".format(a, b, a - b))
    if i == 3:
        print("giridiğiniz {} sayısı ile {} sayısı çarpımı = {} ".format( a, b, a * b))
    if i == 4:
        print("giridiğiniz {} sayısının {} sayısına bölümü  sonucu = {} ".format(a, b, a / b))
    if i == 5:
        print("giridiğiniz {} mod {}  işleminin sonucu = {} ".format(a, b , a % b))
else:
    print("geçersiz işlem numarası")