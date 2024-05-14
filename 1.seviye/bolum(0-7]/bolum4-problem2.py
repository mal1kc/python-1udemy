print(" sırayla 3 adet sayı giriniz en büyüğünü size söyliyim ")
a = float(input("birinci sayıyı giriniz : "))
b = float(input("ikinci sayıyı giriniz : "))
c = float(input("üçüncü sayıyı giriniz : "))

if a > b and a > c:
    enb = a
elif b > a and b > c:
    enb = b
elif c > a and c > b:
    enb =  c

print("en büyük sayı {} ".format(enb))
pass