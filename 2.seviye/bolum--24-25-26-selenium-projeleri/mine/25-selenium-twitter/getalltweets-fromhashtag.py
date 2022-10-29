from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import os.path

gecko_path = os.path.dirname(os.path.dirname(
    __file__))+"\\.selenium_drivers\\geckodriver.exe"

fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.headless=True
browser = webdriver.Firefox(executable_path=gecko_path, options=fireFoxOptions)

# ! disabled this section for spamming
# browser.get("https://twitter.com/")

# time.sleep(3)

# login = browser.find_element_by_xpath(
#     "/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span")

# login.click()


# time.sleep(3)

# username = browser.find_element_by_xpath(
#     "/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
# password = browser.find_element_by_xpath(
#     "/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

# f = open("login_info.json")

# data = json.load(f)

# username.send_keys(data['login']['username'])

# password.send_keys(data['login']['password'])

# login = browser.find_element_by_xpath(
#     "/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span")

# login.click()
# f.close()
# ! search without login


browser.get("https://twitter.com/explore")
time.sleep(2)
search_area = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")
# search_area = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")

search_area.send_keys("#yazilimayolver")
search_area.send_keys(Keys.ENTER)
time.sleep(5)

# * javascript ile scroll
lenOfPage = browser.execute_script( "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while(match == False):
    lastCount = lenOfPage
    time.sleep(4)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    time.sleep(4)
    if lastCount == lenOfPage:
        match = True
time.sleep(5)

elements = browser.find_elements_by_css_selector(".css-901oao.r-1fmj7o5.r-1qd0xha.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0")

with open("tweets.txt", "w", encoding="utf-8") as f:
    tweetCount = 1
    for element in elements:
        print(element.text,
              end="\n-------------------------------------------------------\n")
        f.write((str(tweetCount) + "\n\n" + element.text +
                "\n\n-------------------------------------------------------\n\n"))
        tweetCount += 1


time.sleep(5)
browser.close()
