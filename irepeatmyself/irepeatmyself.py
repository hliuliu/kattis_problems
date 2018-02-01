

def smallest_pf(n):
	i=2
	while 1:
		if not n%i:
			return i
		i+=1

def shortest_pattern_len(s):
	n=len(s)
	for i in xrange(1,n+1):
		for j in xrange(i,n):
			if s[j]!=s[j%i]:
				break
		else:
			return i

n=int(raw_input())

for _ in xrange(n):
	line=raw_input()
	print shortest_pattern_len(line)



