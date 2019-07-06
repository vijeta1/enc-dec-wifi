#!/bin/bash
from subprocess import Popen,PIPE,call,check_output
import hashlib
import random
import math
from random import randrange

def wifisalt():
	def swap(a,b,salt):
	    temp1=salt[a]
	    temp2=salt[b]
	    salt[b]=temp1
	    salt[a]=temp2
	    return

	process2=Popen(['iwgetid'],stdin=PIPE,stdout =PIPE)
	stdout,stderr=process2.communicate()
	stdout=str(stdout)
	stdout=stdout.split('"')
	ssid=stdout[1]
	COMMAND_LINUX = "sudo ls /etc/NetworkManager/system-connections/ | grep "+stdout[1]+" "
	output = check_output(COMMAND_LINUX,shell=True)
	ouutput=str(output)
	wname = ouutput[2:-3]
	COMMAND_LINUX = "sudo cat /etc/NetworkManager/system-connections/"+wname
	output = check_output(COMMAND_LINUX,shell=True)
	output=output.splitlines()
	uuid=str(output[2]).split('=')
	uuidfinal=str(uuid[1]).strip(" - ")
	uuidfinal=uuidfinal.strip(" ' ")
	if 'psk' in str(output[16]):
	    password=str(output[16]).split('=')
	    passwordfinal=str(password[1]).strip(" ' ")
	else:
	    passwordfinal=uuidfinal

	salt=ssid+" "+uuidfinal+" "+passwordfinal


	length=len(salt)
	length=int(length/4)
	salt=list(salt)
	for x in range (length):
	    swap(4*x+1,4*x+2,salt)
	    swap(4*x,4*x+3,salt)
	    swap(4*x,4*x+1,salt)

	salt=''.join(salt)
	salt=salt.encode('utf-8')
	salt=salt.hex()

	#print(salt)

	rand=str(random.randint(0,1000000))

	pepper=hashlib.md5(rand.encode())
	pepper=pepper.hexdigest()
	#print(len(str(pepper)))
	salt=salt+str(pepper)

	num=0
	for i in salt:
	    num=num+ord(i)
	   
	return num 

def decimalToBinary(n):
    rep = ''  	
    while n > 0:  
        rep += str(n%2)
        n = n//2
    return int(rep[::-1])


b=wifisalt()

dx=int(input("Enter the encrypted message : "))
d=dx%1000
dx=dx//1000
print("---------Decrytion---------")
dx=decimalToBinary(dx) #binary of the encrypted decimal
dx=str(dx)
ex=dx[0:27] #message size
ey=dx[27:37] #random value used
ez=dx[37:] #xored message
# size=str(int(ex[1:]))
# size=binaryToDecimal(size)
# print("Size is: ",size)
# rval=binaryToDecimal(str(int(ey[3:])))
# print "rval is:",rval
# print "d is:",d
y = int(ez,2)
for i in range(int(d)):
    po=i*d
    po=po%100000
    y=y^po

msg=y^b
#print("Your Message is : ", y^b) #getting message back
tru=[]
while msg:
    q1=msg%1000
    #print(q1)
    msg=msg//1000
    tru.append(chr(int(q1)))
tru1=tru[::-1]


print(''.join(tru1))
