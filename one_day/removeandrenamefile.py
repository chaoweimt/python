#-*- coding:UTF-8 -*-
#remove file and rname file
import os
d = os.listdir(os.getcwd())
print(d)
def removefile():
	os.remove("remove.txt")

def renamefile():
	for f in d:
		if f =='test.txt':
			os.rename(f,"read.txt")

		if f == 'mytest.txt':
			os.rename(f,"write.txt")





renamefile()
removefile()