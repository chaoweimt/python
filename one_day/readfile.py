#-*- coding:UTF-8 -*-

def readfile():
	f = open("test.txt",'r')

	firstline = f.readline()
	secondline = f.readline()
	print(firstline)
	print(secondline)
	f.close()

readfile()