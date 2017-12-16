
import string

line=raw_input().strip()

ws,lc,uc=0,0,0

n=len(line)

for c in line:
	if c=='_':
		ws+=1
	elif c in string.ascii_lowercase:
		lc+=1
	elif c in string.ascii_uppercase:
		uc+=1


for i in [ws,lc,uc,n-lc-uc-ws]:
	print float(i)/n





