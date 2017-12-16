

n=int(raw_input())

v=0
for i in xrange(n):
	s=int(raw_input())
	v+=(s/10)**(s%10)

print v



