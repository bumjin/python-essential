#!/usr/bin/env python

class house:

	doors = 2
	__cost = 120000

	def addDoors(self, number):
		self.doors = number

	def slamDoors(self):
		for door in range(self.doors):
			print "SLAM!"
		print "that's a lot of slamming for a house that costs ", self.__cost

myHouse = house()
#myHouse.doors = 15
print myHouse.doors
myHouse.addDoors(10)
myHouse.slamDoors()

#print myHouse.__cost