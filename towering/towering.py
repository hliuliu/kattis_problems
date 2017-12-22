


line=map(int,raw_input().split())

boxes=line[:6]
hts=line[6:]

def ss3():
	for i in xrange(4):
		for j in xrange(i+1,5):
			for k in xrange(j+1,6):
				yield (i,j,k)



for i,j,k in ss3():
	if sum([boxes[n] for n in (i,j,k)]) in hts:
		b1=[]
		for n in (k,j,i):
			b1.append(boxes.pop(n))
		b1.sort(reverse=True)
		boxes.sort(reverse=True)
		if sum(b1)==hts[1]:
			b1,boxes=boxes,b1
		print ' '.join(map(str,b1+boxes))
		break



