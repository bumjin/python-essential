#!/usr/bin/env python

class house:

	def __init__(self, doors=3):
		self.doors = doors

	def addDoors(self, number):
		self.doors = number

	def slamDoors(self):
		for door in range(self.doors):
			print "SLAM!"
		print "that's a lot of slamming for a house that costs ", self.__cost

class castle(house):
	
	def fireCannons(self, number):	
		for cannon in range(number):
			print "firing cannon number", number, "boo"
	
	def payMortgage(self):
		print "readying the cannons!"

class  apartment(house):
	
	def payMortgage(self):
		print "here's your money"

landloardsProperties = [castle(), apartment()]

for house in landloardsProperties:
	house.payMortgage()