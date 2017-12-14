

_,p=map(int,raw_input().split())

probs=map(int,raw_input().split())

first=probs.pop(p)

probs.sort()

probs.insert(0,first)


elapsed=0
penalty=0
numsolved=0

for q in probs:
	if elapsed+q>300:
		print numsolved,penalty
		break
	elapsed+=q
	penalty+=elapsed
	numsolved+=1
else:
	print numsolved,penalty



