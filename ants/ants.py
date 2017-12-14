

m = int(raw_input())




def readn_int(n):
	l=[]
	while len(l)<n:
		l.extend(map(int,raw_input().strip().split()))
	return l



def shortest(pos,l):
	return max((min(p,l-p) for p in pos))

def longest(pos,l):
	return max((max(p,l-p) for p in pos))




for i in xrange(m):
	l,n= map(int,raw_input().strip().split())
	pos=readn_int(n)
	#print pos
	print shortest(pos,l),longest(pos,l)







