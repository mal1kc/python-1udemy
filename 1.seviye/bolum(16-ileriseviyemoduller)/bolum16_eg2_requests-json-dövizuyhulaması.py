import requests
import sys

url = "http://data.fixer.io/api/latest?access_key=***REMOVED***"

# birinci_doviz = input("Birinci Döviz:").upper()
# ikinci_doviz = input("İkinci Döviz:").upper()
# miktar = float(input("Miktar:"))

response = requests.get(url)

json_verisi = response.json()
sonuc = float()
allsw = list()
for i, j in json_verisi["rates"].items():
    allsw.append(i + "\t" + str(j)+"€\t")
for i in allsw:
    print(i,end="")

# try:
#     if json_verisi["rates"][birinci_doviz] > json_verisi["rates"][ikinci_doviz]:
#         sonuc = (json_verisi["rates"][birinci_doviz] / json_verisi["rates"][ikinci_doviz]) * miktar
#         print("{0:,.2f} {1} = {3:,.2f} {2}".format(miktar, ikinci_doviz, birinci_doviz, sonuc))
#     else:
#         sonuc = (json_verisi["rates"][ikinci_doviz] / json_verisi["rates"][birinci_doviz]) * miktar
#         print("{0:,.2f} {1} = {3:,.2f} {2}".format(miktar, birinci_doviz, ikinci_doviz, sonuc))
# except KeyError:
#     sys.stderr.write("Lütfen para birimlerini doğru girin")
#     sys.stderr.flush()
