
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.BOLD + "1 bilinmeyenli 2.dereceden denlem çözücü ilk sürüm" + color.END)
a = float(input("kareli bilinmeyenin önündeki sayıyı giriniz = "))
while (a == 0 ):
   print("kareli bilinmeyenin önündeki sayı " + color.BOLD + color.RED + "0 olursa 2. derceden denklem olmaz " + color.END + "." )
   a = float(input("kareli bilinmeyenin önündeki sayıyı tekrar giriniz = "))

b = float(input("bilinmeyenin önündeki sayıyı giriniz = "))
c = float(input("sabit terim olan sayıyı giriniz = "))
print("hesaplanıyor.. .")
delta = ((b ** 2) - (4 * a * c))
x1 = ((-b - (delta ** 0.5) / (2 * a)))
x2 = ((-b + (delta ** 0.5) / (2 * a)))
bilinmeyenler = [x1, x2]
print(color.BOLD)
print("1.bilinmeyen = {}\n2.bilinmeyen = {}\n".format(bilinmeyenler[0], bilinmeyenler[1]))
print(color.END)