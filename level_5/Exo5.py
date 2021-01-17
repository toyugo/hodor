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
    """if len(capcha2) == 4:
        r = session.post(pageName, cookies = cookies, headers = headers, data = {'id':'2490','key': key1,'holdthedoor':'Envoyer','captcha': capcha2})
        print(r.text)
        return(True)
    else:
        return(False)"""
def ImageAnalysis():
	ls = {}
	i = Image.open('/Users/olivierguyot/vagrant1/sharedFolder/scraptest/test.png')
	x = 10
	y = 10
	cp = 0
	for x in range(0, 200):
		for y in range(0,30):
			px = i.getpixel((x,y))
			print("Analysis : x={}, y={}, px={}".format(x,y,px))
			ls[str(px)] = str(cp)
			cp += 1
	print(ls)
	(red,green,blue) = i.getpixel((x,y))
	print (red, green, blue)
def ImageAnalysis2(img_path):
	ls = {}
	i = Image.open(img_path)
	img = cv2.imread(img_path)
	img = cv2.GaussianBlur(img, (5,5), 0)
	#img = cv2.medianBlur(img,5)
	dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
	print(dst)
	b,g,r = cv2.split(dst)  
	rgb_dst = cv2.merge([r,g,b])
	print(img.shape)
	c = 1
	cv2.imwrite('/Users/olivierguyot/vagrant1/sharedFolder/scraptest/retreate.png', img)
def Imageretreatv2():
	im_noise = Image.open('/Users/olivierguyot/vagrant1/sharedFolder/scraptest/test.png')
	im_med = ndimage.median_filter(im_noise, 3)
	io.imsave('/Users/olivierguyot/vagrant1/sharedFolder/scraptest/retreate2.png', im_med)
	#im_med.save('')
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

    with open('/Users/olivierguyot/vagrant1/sharedFolder/scraptest/test.png', 'wb') as f:
        f.write(img.content)
        f.close()
    im_noise = Image.open('/Users/olivierguyot/vagrant1/sharedFolder/scraptest/test.png')
    im_med = ndimage.median_filter(im_noise, 3)
    io.imsave('/Users/olivierguyot/vagrant1/sharedFolder/scraptest/retreate2.png', im_med)
    capcha = pytesseract.image_to_string(Image.open('/Users/olivierguyot/vagrant1/sharedFolder/scraptest/retreate2.png'))
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
#ImageAnalysis2('/Users/olivierguyot/vagrant1/sharedFolder/scraptest/test.png')
def denoising():
	import numpy as np
	from scipy import ndimage
	import matplotlib.pyplot as plt

	im = np.zeros((20, 20))
	im[5:-5, 5:-5] = 1
	im = ndimage.distance_transform_bf(im)
	im_noise = im + 0.2*np.random.randn(*im.shape)

	im_med = ndimage.median_filter(im_noise, 3)

	plt.figure(figsize=(16, 5))
	plt.subplot(141)
	plt.imshow(im, interpolation='nearest')
	plt.axis('off')
	plt.title('Original image', fontsize=20)
	plt.subplot(142)
	plt.imshow(im_noise, interpolation='nearest', vmin=0, vmax=5)
	plt.axis('off')
	plt.title('Noisy image', fontsize=20)
	plt.subplot(143)
	plt.imshow(im_med, interpolation='nearest', vmin=0, vmax=5)
	plt.axis('off')
	plt.title('Median filter', fontsize=20)
	plt.subplot(144)
	plt.imshow(np.abs(im - im_med), cmap=plt.cm.hot, interpolation='nearest')
	plt.axis('off')
	plt.title('Error', fontsize=20)
	plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0,
                    right=1)
	plt.show()

