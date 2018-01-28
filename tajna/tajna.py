
from math import sqrt

msg = raw_input()

n=len(msg)

r= int(sqrt(n))

while n%r:
	r-=1

c=n//r

msgarray=[[0]*c for _ in xrange(r)]

for i,w in enumerate(msg):
	msgarray[i%r][i//r]=w

print ''.join(map(lambda row: ''.join(row),msgarray))

