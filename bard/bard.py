

bits=[1]

for _ in xrange(50):
	bits.append(bits[-1]<<1)


n=int(raw_input())
e=int(raw_input())


villagers=[0]*(n+1)


def bor(line):
	x=0
	for p in line:
		x|=villagers[p]
	return x

songnum=0

for _ in xrange(e):
	line=map(int,raw_input().split())
	line.pop(0)
	if 1 in line:
		for p in line:
			villagers[p]|=bits[songnum]
		songnum+=1
	else:
		common=bor(line)
		for p in line:
			villagers[p]=common


for i in xrange(1,n+1):
	if villagers[i]==villagers[1]:
		print i







