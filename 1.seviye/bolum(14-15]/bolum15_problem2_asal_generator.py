def asal_mi(sayi):
    j = 2
    if sayi == 1:
        return False
    elif sayi == 2:
        return True
    else:
        while sayi > j:
            if sayi % j == 0:
                return False
            j += 1
        return True


def asaluret():
    say1 = 2
    while True:
        if asal_mi(say1):
            yield say1
        say1 += 1


for i in asaluret():
    if i > 20000:
        break
    print(i)
