# "Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. Bu sınıfın init
# fonksiyonu maksimum isimli bir tane parametre alsın ve her next işleminde ekrana üzerinde bulunduğunuz sayının
# karesi yazdırılsın. StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın.

class Kareler:
    def __init__(self, maks=0):
        self.maks = maks
        self.sayi = maks - (maks - 1)

    def __iter__(self):
        return self

    def __next__(self):
        if self.sayi <= self.maks:
            sonuc = self.sayi * self.sayi
            self.sayi += 1
            return sonuc
        else:
            self.kuvvet = 0
            raise StopIteration


kareler = Kareler(7)

for i in kareler:
    print(i)
print("\n")
iteration = iter(kareler)
while True:
    next(iteration)
