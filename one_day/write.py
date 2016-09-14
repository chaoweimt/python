#-*- conding:UTF-8 -*-
#file write

def write():
	f = open('mytest.txt','w')

	f.write("Python is an interesting programming language.\n It is so powerful that I have to have a strong interest in it.")
	f.flush()
	f.close()


write()