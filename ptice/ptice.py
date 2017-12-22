
people= ['Adrian','Bruno','Goran']

seqs=zip(people,['ABC','BABC','CCAABB'])

raw_input()
answers=raw_input()

nc=dict(zip(people,[0]*3))


for p,s in seqs:
	for i,c in enumerate(answers):
		if c==s[i%len(s)]:
			nc[p]+=1

m=max(nc.values())
print m
for p in people:
	if nc[p]==m:
		print p


