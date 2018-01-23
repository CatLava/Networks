# geolocate IPs with higher precision than shodan will provide

import json
import urllib.request, urllib.parse, urllib.error

testurl = 'http://freegeoip.net/json/73.241.193.214'
url = urllib.request.urlopen(testurl)
data = url.read().decode()
#print('Retreived', len(data))
js = json.loads(data)
#print(js)
def loc(deol):
    test = 'http://freegeoip.net/json/{}'.format(deol)
    url1 = urllib.request.urlopen(test)
    data1 = url1.read().decode()
    js1 = json.loads(data1)
    return js1
