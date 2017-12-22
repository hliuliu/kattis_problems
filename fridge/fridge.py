

ostr='1234567890'

line= raw_input()

cnts=dict(zip(ostr,[0]*10))

for c in line:
	cnts[c]+=1

def comp():
	mv=min(cnts.values())
	for i in ostr:
		if cnts[i]==mv:
			if int(i):
				return i*(cnts[i]+1)
			return '1'+'0'*(cnts[i]+1)


print comp()


