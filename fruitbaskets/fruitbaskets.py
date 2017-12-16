

def prefsum(wts):
	ps=[0]
	a=0
	for w in wts:
		a+=w
		sm.append(a)
	return ps



raw_input()

wts=map(int,raw_input().split())
ss=sum(wts)<<(len(wts)-1)


wts.sort()

while wts and wts[-1]>=200:
	wts.pop()



def genwts(wts,acc=0):
	if acc<200:
		if not wts:
			yield acc
		else:
			v=wts.pop()
			for i in genwts(wts,acc+v):
				yield i
			for i in genwts(wts,acc):
				yield i
			wts.append(v)



#print ss

print ss-sum(genwts(wts))







