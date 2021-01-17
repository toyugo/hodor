#!/usr/bin/python3
import requests
cp = 0
for i in range(0, 1024):
    r = requests.post('http://158.69.76.135/level0.php', data = {'id':'2490', 'holdthedoor':'Envoyer'})
    print(r)
    cp = cp + 1
print(cp)
