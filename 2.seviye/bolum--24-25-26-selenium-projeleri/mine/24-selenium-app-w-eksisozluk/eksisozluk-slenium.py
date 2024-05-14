from selenium import webdriver
import random
import time

import os.path

gecko_path = os.path.dirname(os.path.dirname(__file__))+"\\.selenium_drivers\\geckodriver.exe"

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
browser = webdriver.Firefox(executable_path=gecko_path,firefox_options=fireFoxOptions)
elements = []
pageCount = 1
url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
while pageCount <= 3:
    randomPage = random.randint(1,1290)
    newUrl = url +str(randomPage)
    print("şuanda bulunduğu adres : " + str(newUrl))
    browser.get(url=newUrl)
    page_elements = (browser.find_elements_by_css_selector('.content')) 
    for element in page_elements:
        elements.append(element.text)
    time.sleep(3)  
    pageCount += 1

with open("entries.txt","w",encoding="utf-8")as f:
    for element in elements:
        print(element,end="\n**************************\n")
        f.write(str(element +"\n**************************\n"))


browser.close()

