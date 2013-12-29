#!/usr/bin/env python

name = raw_input('Plaese type in your name: ')

if len(name) < 5:
	print	"Your name has fewer than 5 chracters"
elif len(name) == 5:
	print "Your name hs exactly 5 chracters"
	if name == 'Jesse':
		print "Hey Jesse!"
else:
	print	"Your name has greater than 5 chracters"