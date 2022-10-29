# Problem 1
#
# Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.
#
# liste = ["345","sadas","324a","14","kemal"]
#
# Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. Bunu yaparken try,
# except bloklarını kullanmayı unutmayın.
liste = ["345", "sadas", "324a", "14", "kemal"]


def liste_sayiyaz(index):
    try:
        temp = liste[index]
        print(int(temp))
    except ValueError:
        pass


for i in range(0, len(liste)):
    liste_sayiyaz(i)

# Problem 2
#
# Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise return ile bu
# değeri dönsün. Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın. Daha sonra, içinde çift ve
# tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.

print("\n\nproblem 2 ye gecti \n\n")


def tek_cift(girdi):
    if girdi % 2 == 0:
        return girdi
    else:
        raise ValueError("bu sayı tek")


liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0, 10, 11, 22, 34, 67, 989, 456]

for i in liste:
    try:
        print(tek_cift(i))
    except ValueError:
        pass
