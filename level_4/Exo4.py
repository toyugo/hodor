"""
setup:
    pip install requests
    PySocks
    stem ( to control tor)

super helpful:
    - http://packetforger.wordpress.com/2013/08/27/pythons-requests-module-with-socks-support-requesocks/
    - http://docs.python-requests.org/en/master/user/advanced/#proxies
    
test tor launchged : curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/ | cat | grep -m 1 Congratulations | xargs
pysocks ( not polipo)
    """
import requests
import time
from PIL import Image
from stem import Signal
from stem.control import Controller

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
def Getproxy(filepath):
    proxyRes = []
    fichier = open(filepath, 'r')
    for i in fichier:
        file1 = i.split(' ')[0]
        proxyRes.append(file1)
    print(proxyRes)
    return(proxyRes)
def GetPageRequest(pageName):
    #session = requests.Session()
    with Controller.from_port(port = 9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)
        delay = c.get_newnym_wait()
        c.close()
    time.sleep(delay)
    session = requests.Session()
    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8", 
        "Accept-Encoding": "gzip, deflate", 
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7", 
        "Host": "158.69.76.135",
        "Referer": pageName,
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }
    session.headers.update(headers)
    proxies = {}
    session.proxies['http'] = 'socks5://127.0.0.1:9050'
    session.proxies['https'] = 'socks5://127.0.0.1:9050'
    r = session.get(pageName, proxies=proxies)
    cookies = r.cookies.get_dict()
    print(cookies)
    key1 = cookies.get('HoldTheDoor')
    print (cookies)
    r = session.post(pageName, cookies = cookies, data = {'id':'2490','key': key1,'holdthedoor':'Envoyer'})
    print("###########")
    print(session.proxies)
    print("###########")
    print(r.text)
#GetPageRequest('https://www.google.com')
#Getproxy('/Users/olivierguyot/vagrant1/sharedFolder/scraptest/proxylist.txt')
for i in range(0, 1):
    print("#################" + str(i))
    GetPageRequest('http://158.69.76.135/level4.php')
#GetPageRequest('http://httpbin.org/ip')
#GetPageRequest('http://httpbin.org/ip')
#GetPageRequest('http://httpbin.org/ip')
