#!/usr/bin/env python

def dbLookup():
	dict = {}
	dict['amazon'] = 100
	dict['ebay'] = 120
	dict['bestBuy'] = 34
	return dict



def shoppingCart3(itemName, avgPrices):
	print 'item', itemName
	for price in avgPrices:
		print price, 'price', avgPrices[price]

#print dbLookup()
shoppingCart3('computer', dbLookup())

def madlib(adjective='thristy', name='adam'):
	print "the %s %s ate all the pizza" % (adjective,name)

#madlib(adjective='hungry', name='bumjin')


def shoppingCart(itemName, *avgPrices):
	for price in avgPrices:
		print 'price', price

#shoppingCart('computer', 100, 120, 34)

def shoppingCart2(itemName, **avgPrices):
	print avgPrices
	for price in avgPrices:
		print price, 'price', avgPrices[price]

#shoppingCart2('computer', amazon=100, ebay=120, bestBuy=34)