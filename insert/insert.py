


def choose(n,r):
	if r*2>n:
		r = n-r
	ans = 1
	for i in xrange(r):
		ans *= n-i
		ans /= i+1
	return ans




def build(seq):
	if not seq:
		return 1
	low, high = [],[]
	root = seq.pop(0)
	for x in seq:
		(low if x<root else high).append(x)

	n = len(seq)
	m = len(high)
	return build(low)*build(high)*choose(n,m)







n = int(raw_input())

while n:
	seq = map(int, raw_input().split())
	print build(seq)
	n = int(raw_input())


