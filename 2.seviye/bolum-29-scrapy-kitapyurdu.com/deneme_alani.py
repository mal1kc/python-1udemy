import json

with open(r"mine\scrapy-kitapyurdu\kitapyurdu\books.json","r",encoding="utf-8") as f:
    before_data = json.load(f)
    print(before_data)

file = open(r"mine\scrapy-kitapyurdu\kitapyurdu\books.json","w",encoding="utf-8")
jsonouts = list()
page = 2
after_data = dict()
itemnumber = 0
for i in before_data.keys():
    after_data[i] = before_data[i] 

temp_list = list(before_data)
after_data[f"page_{page}"] = dict()
for i in temp_list:
    after_data[f"page_{page}"][str(itemnumber)] = i 
    itemnumber +=1  

jsonouts.append(json.dumps(after_data,indent=4))
for i in jsonouts:
    # print(i)
    file.write(i)
file.close()
