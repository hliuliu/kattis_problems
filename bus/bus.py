

table=[0]*31

for i in xrange(1,31):
	table[i]=(table[i-1]<<1)+1


t=int(raw_input())

for _ in xrange(t):
	print table[int(raw_input())]



