import urllib2, json
x = float(json.loads(urllib2.urlopen('https://mtgox.com/api/1/BTCUSD/ticker').read())['return']['last']['value'])
print x

