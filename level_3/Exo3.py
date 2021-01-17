#!/usr/bin/python3
import requests
import time
from pprint import pprint
import pytesseract
from PIL import Image
from selenium import webdriver

def GetPage(pageName):
    c = True
    opts = webdriver.chrome.options.Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
    chromeProfilePath = "/Users/olivierguyot/vagrant1/sharedFolder/scraptest/tempfile/"
    #opts.add_argument("user-data-dir=" + chromeProfilePath)
    driver = webdriver.Chrome(options=opts)
    driver.get(pageName)
    print("ELEMENT")
    #element = driver.find_element_by_xpath('//img')
    element = driver.find_element_by_tag_name('h1')
    print(element)
    while (c):
        pass
def GetPageRequest(pageName):
    session = requests.Session()
    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8", 
        "Accept-Encoding": "gzip, deflate", 
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7", 
        "Host": "158.69.76.135",
        "Referer": pageName,
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        }
    r = session.get(pageName)
    cookies = r.cookies.get_dict()
    key1 = cookies.get('HoldTheDoor')
    #print(r.text)
    img = session.get('http://158.69.76.135/captcha.php')

    with open('/Users/olivierguyot/vagrant1/sharedFolder/scraptest/test.png', 'wb') as f:
            f.write(img.content)
            f.close()
    capcha = pytesseract.image_to_string(Image.open('/Users/olivierguyot/vagrant1/sharedFolder/scraptest/test.png'))
    capcha = capcha.replace("\n", "")
    capcha2 = ""
    for i in capcha:
        if i.isalnum():
            capcha2 += i
    print(capcha2)
    if len(capcha2) == 4:
        r = session.post(pageName, cookies = cookies, headers = headers, data = {'id':'2490','key': key1,'holdthedoor':'Envoyer','captcha': capcha2})
        print(r.text)
        return(True)
    else:
        return(False)
cp = 829
while cp <= 1024:
    if GetPageRequest("http://158.69.76.135/level3.php") == True:
        cp += 1
        print("True {}".format(cp))
    else:
        print("Fail")
    time.sleep(1)
