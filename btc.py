import urllib2, json
rate = float(json.loads(urllib2.urlopen('https://www.bitstamp.net/api/ticker/').read())['last'])
print rate

