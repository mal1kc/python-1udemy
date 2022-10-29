from platform import win32_edition
from selenium import webdriver
import time
import os.path
import json

f = open("login_info.json")

data = json.load(f)

gecko_path = os.path.dirname(os.path.dirname(os.path.dirname(
    __file__)))+"\\.selenium_drivers\\geckodriver.exe"

fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.headless=True
browser = webdriver.Firefox(executable_path=gecko_path, options=fireFoxOptions)

browser.get("https://www.instagram.com/")

time.sleep(2)

login_button = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")

username = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")

password = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")

username.send_keys(data["login"]["username"])
password.send_keys(data["login"]["password"])

f.close()
login_button.click()

time.sleep(5)

skip = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div/div/div/button")
skip.click()
time.sleep(3)
try:
    skip = browser.find_element_by_xpath(
        "/html/body/div[5]/div/div/div/div[3]/button[2]")
    skip.click()
except Exception as err:
    skip = browser.find_element_by_css_selector(
        "html.js.logged-in.client-root.js-focus-visible.sDN5V body div.RnEpo.Yx5HN div.pbNvD.fPMEg div._1XyCr div.piCib div.mt3GC button.aOOlW.HoLwm")
    skip.click()
    with open("err.txt", "w", encoding="utf-8") as f:
        f.write("hata oluştu")
        f.write(str(browser.context))
        f.write("\n")
        f.write(str(err))
        f.write("\n")

time.sleep(3)

profile_button = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a")

profile_button.click()

time.sleep(2)

followers_button = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")

followers_button.click()

time.sleep(10)

# * javascript ile scroll

jscommand = """
followers=document.querySelector(".isgrP");
followers.scrollTo(0,followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;
"""

lenOfPage = browser.execute_script(jscommand)
match = False
while(match == False):
    lastCount = lenOfPage
    time.sleep(2)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match = True
time.sleep(5)

followers = browser.find_elements_by_css_selector("a.FPmhX.notranslate._0imsa")
# followerslist = list()
# for follower in followers:
#     followerslist.append(follower.text)

with open("followers.txt", "w", encoding="utf-8") as f:
    followerCount = 0
    for follower in followers:
        print(follower.text,
              end="\n-------------------------------------------------------\n")
        f.write((str(followerCount) + "\n\n" + follower.text +
                 "\n\n-------------------------------------------------------\n\n"))
        followerCount += 1

browser.close()
exit()
