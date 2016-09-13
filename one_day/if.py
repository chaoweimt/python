#-*- coding:UTF-8 -*-
#if 语句的操作
def guess():
    s = input("please input number:")
    if int(s) ==0 :
        print("congratulations you are right!!!")
        return
    else :
	    print("sorry plaese input number again ...")
	    guess()

	    
guess()