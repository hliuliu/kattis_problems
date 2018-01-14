
from math import pi
from string import ascii_uppercase as au

unit = 15*pi/7


chars = {i:j for j,i in enumerate(au+' \'')}

def getdist(a,b):
	dist = abs(chars[a]-chars[b])
	return min(dist, 28-dist)*unit

n = int(raw_input())


while n:
	n-=1
	msg = raw_input()
	d = 0
	for i in xrange(1,len(msg)):
		d+= getdist(msg[i-1],msg[i])
	print d/15+len(msg)

