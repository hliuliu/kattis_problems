


digits=map(int,raw_input().strip())

'''
for i in xrange(len(digits)-1,0,-1):
	if digits[i]>digits[i-1]:
		digits[i],digits[i-1]=digits[i-1],digits[i]
		digits[i:]=sorted(digits[i:])
		print ''.join(map(str,(digits)))
		break
else:
	print 0
'''


def gen(dgs):
	if not dgs:
		yield []
	else:
		used=set()
		for i in xrange(len(dgs)):
			if dgs[i] in used:
				continue
			used.add(dgs[i])
			for j in gen(dgs[:i]+dgs[i+1:]):
				yield [dgs[i]]+j


def tonum(dgs):
	a=0
	for d in dgs:
		a=a*10+d
	return a


sdigits=sorted(digits)

for ds in gen(sdigits):
	if ds>digits:
		print tonum(ds)
		break
else:
	print 0






