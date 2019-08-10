<------------------------------	NETWORK ENCRYPTION README ------------------------------------>

			Summer project of Cyber Security wing Geekhaven IIIT Allahabad

-------------------------------------
README covers the following points- |
-------------------------------------
->About the project
->AIM/Target Audience
->What does it do?
->System Prequisites
->Instllation and use
->How to use
->Refernces



---------
About : |
---------
This project aims Encryption and Decryption of message using Wifi network.



-----------------------
AIM/Target Audience : |
-----------------------
The softwares in the organization which are used to communicate confidential information over the browser. 



------------------
What Does it do? |
------------------
It encrypts the network information in the way that even if the message is intercepted would be not readable or decryptible by the person. Even if the sam emessage is sent twice it may not be same string transmitted. This increases the data security as it won't show any type of redundancy of the  encrypted text making it impossible for the malicious end to decipher new text through known encrypted and actual texts.
This technology is router specific.It uses basic router information like BSSID,wifiname,etc to encrypt the text.This increases data security within an organisation.



---------------------
System Prequisites: |
---------------------
The codes would run only on LINUX systems with Python 3
                    ----    -------------      --------
This is because the normal data tranmission use linux extensively and which would increase a layer of network security through a big leap.



-----------------------
Installation and use: |
-----------------------
Linux can be downloaded from https://www.linux.org/pages/download/
				   -------------------------------
You can install Python 3 in your linux system from https://www.python.org/downloads/
						   ---------------------------------
The project has two files named encrypt.py and decrypt.py
				----------     ----------
Let's see how do you apply this to your software(example: router software).
Let a project domain WIFI netwrok be X(ex: the main organizational network over which teh work is done). The text in the server would have to passed through the encrypt.py function to get stored. And to retrieve it the text shown would be the text passed through decrypt.py code. If the user has the access to the network used officially, then he would see the exact written information else the user will see some random strings.

-----------------------
How to use           :|
-----------------------
for encryption->
python3 encrypt.py
for decryption->
python3 decrypt.py



-----------------------
References          : |
-----------------------
https://www.idiotinside.com/2015/02/16/how-to-find-saved-wifi-password-via-command-line-in-ubuntu/
https://stackoverflow.com/questions/42173991/how-to-get-the-bssid-of-currently-connected-network-through-bash

