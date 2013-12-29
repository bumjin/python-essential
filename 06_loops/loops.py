#!/usr/bin/env python

languages = ['python', 'java', 'C++', 'PHP']

for language in languages:
	print language, "rocks!"
	
dict = {"name":"Jesse","location":"Denver","favorite site":"tutsplus"}

for key in dict:
	print "His ", key, "is", dict[key]

print range(10)

for int in range(10):
	print "int =", int
	if int == 5:
		break
print "done looping"

count = 0
while count < 10:
	print count, "count is less than 10"
	count +=1

for i in range(2):
	print "this is before continue"
	continue
	print "this is after the continue statement"

for i in range(2):
	pass