print("""
-------------------------------
Fibonacci serisi oluşturucu v1

--------------------------------
""")
a = 1
b = 1
fibonacci = [a, b]

sira = int(input("fibonacci serisini kaçıncı sayıya kadar istiyorsunuz  : "))

for i in range(sira):
    a, b = b, a + b
    fibonacci.append(b)
    print(fibonacci)
print("sonuc \n", fibonacci)
