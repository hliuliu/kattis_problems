

n= int(raw_input())

ct1,ct2={},{}
dres=set()

for _ in xrange(n):
	res=raw_input()
	dres.add(res)
	ct1[res]=ct1.get(res,0)+1

for _ in xrange(n):
	res=raw_input()
	dres.add(res)
	ct2[res]=ct2.get(res,0)+1

s=0
for res in dres:
	s+=min(map(lambda d: d.get(res,0),[ct1,ct2]))

print s



