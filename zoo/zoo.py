

cs=1
n=int(raw_input())

while n:
	d={}
	for _ in xrange(n):
		animal=raw_input().split()[-1].lower()
		d[animal]=d.get(animal,0)+1
	print 'list %d:'%cs
	for a in sorted(d):
		print a,'|',d[a]
	n=int(raw_input())
	cs+=1



