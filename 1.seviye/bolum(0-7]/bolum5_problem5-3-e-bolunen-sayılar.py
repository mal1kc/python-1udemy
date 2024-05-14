"""

Problem 5

1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.

"""

print("""--------------------------------------------------------------
 0 ile verilen sayı arasında 3 bölünen sayıları bulan program
--------------------------------------------------------------""")
bolen = int(input("0 ile kaç arasında bulmak istiyorsunuz : "))
list = []
for i in range(2, bolen + 1):

    if i % 3 != 0:
        continue
    print(i)
    list.append(i)
print(list)
