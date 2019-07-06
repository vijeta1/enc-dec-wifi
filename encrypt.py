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

def binaryToDecimal(binary):
    binary = int(binary, 2)
    return int(binary)

# def rxor(a,b):
#     x = max(a,b)
#     y = min(a,b)
#     diff = len(str(x))-len(str(y))
#     temp = int(y)*pow(10,diff)
#     if diff != 0:
# 	    temp += y//pow(10,(len(str(y))-diff))
#     y = temp
#     result = ''
#     for i in range(len(str(x))):
#         result += str(int(str(x)[i])^int(str(y)[i]))
#     return result

def nthprime(p):
    no= int(p)
    infile = open('primes.txt', 'r')
    lines = infile.readlines()
    count = 0
    for line in lines:
        count+=1
        if count is no:
            return number
    infile.close()
    return 0

a1 = (input('Enter Message: '))
a=0

for i in a1:
    a=a+ord(i)
    a=a*1000
#print(a)
# a is message
le=len(str(decimalToBinary(a)))
b = wifisalt()
#b is wifi salt

print("---------Encrytion---------")

ul=int('0b111111111',2) #upper limit of random value
ll=int('0b1111',2) #lower limit of random value
d=random.randrange(ll,ul) #random value 
y=a^b 
po=1
for i in range(int(d)):
    po=i*d
    po=po%100000
    y=y^po
#xored with every prime
dy=str(decimalToBinary(d))
while len(dy) is not 9:
    dy = '0'+dy
dy = int('1' + dy)
#10 digit binary of random
dy = int(str(dy) + str(decimalToBinary(y)))
#appended random
dx=str(decimalToBinary(le))
while len(dx) is not 26:
    dx = '0'+dx
    # print("inside-loop")
dx = int('1' + dx)
#converted binary length to 27 digits
dx='0b'+str(dx)
dx=int(dx,2)
dx=str(decimalToBinary(dx))
dx = int(dx+ str(dy))
dx='0b'+str(dx)
#print(dx)
dx=int(dx,2)
dx=dx*1000
dx=dx+d
print("Your encrypted message: ", dx) #decimal of the encrypted binary





