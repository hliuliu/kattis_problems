

import re

n= int(raw_input())


while n:
	msg=raw_input()
	msg=msg.upper()
	msg=''.join(re.split('[^A-Z]+',msg))
	if len(msg)<=n:
		cipher=msg
	else:
		cipher=[0]*len(msg)
		pos=0
		start=0
		for c in msg:
			cipher[pos]=c
			pos+=n
			if pos>=len(msg):
				start+=1
				pos=start
		cipher=''.join(cipher)
	print cipher
	n= int(raw_input())



