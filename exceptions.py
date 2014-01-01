#!/usr/bin/env python

try:
	open('fakefile')
#except IOError:
except:
	print "Unable to open file"
else:
	print "No problem opening the file"
finally:
	print "cleaning up code here"

print "this is important"

class DinnerError(Exception):
	pass

def makeDinner():
	userinput = raw_input("Please choose a dinner item: ")
	if userinput == "ice cream":
		raise DinnerError("Not nutritions enough!")
	if userinput == "computer":
		raise DinnerError("Not dinner enough!")

try:
	makeDinner()
except DinnerError, explanation:
		print "Error:", explanation
