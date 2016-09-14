#-*- coding:UTF-8 -*-
#append file

def appendfile():
	f = open('append.txt','a')

	f.write("python is fun\n")
	f.write("on is one \n")
	f.write("https://www.google.com\n")
	f.write("http://www.baidu.com\n")
	f.flush()

	f.close()


appendfile()