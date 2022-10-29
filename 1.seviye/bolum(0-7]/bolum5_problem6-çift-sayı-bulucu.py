'''


Problem 6

Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur. Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.

İpucu: Basit düşünmeye çalışın.


'''

print("""--------------------------------------------------------------
 0 ile verilen sayı arasında 2 ye bölünen sayıları bulan program
--------------------------------------------------------------"""),
bolunen = int(input("0 ile kaç arasında bulmak istiyorsunuz : "))

liste1 = [x for x in range(1,bolunen+1) if x % 2 == 0]
print(liste1)