#-*- coding:UTF-8 -*-
# class car

class car:

	color = 'red'
	oil = 200
	city = 'beijing'

	def __init__(self,othercolor,otheroil,othercity):
		self.othercolor = othercolor
		self.otheroil = otheroil
		self.othercity = othercity

	def jiayou(othercolor,otheroil):
		print(othercolor)
		return otheroil

	def travel():
	    return "西安"

# car = car("blue",300,"guangzhou")
# print(car.color)
# print(car.oil)
# print(car.city)
print(car.jiayou("orange",12000))
print(car.color)
print(car.oil)
print(car.city)
print(car.travel())