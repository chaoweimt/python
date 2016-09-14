#-*- conding:UTF-8 -*-
# read and write file

def readandwritefile():
	read = open('test.txt','r')
	write = open('mytest.txt','w')

	for f in read:
		write.write(f)

	read.close()
	write.close()


readandwritefile()