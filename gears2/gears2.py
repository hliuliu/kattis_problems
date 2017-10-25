
import fractions

n=int(raw_input())

class gear(object):
	def __init__(self,x,y,r):
		self.x=x
		self.y=y
		self.r=r


V=[]

for i in xrange(n):
	V.append(gear(*(map(int,raw_input().split()))))

E=[[0]*n for i in xrange(n)]

def sqdist(g1,g2):
	return (g1.x-g2.x)**2+(g1.y-g2.y)**2

def touch(g1,g2):
	return sqdist(g1,g2)<=(g1.r+g2.r)**2


for i in xrange(n):
	for j in xrange(i+1,n):
		if touch(V[i],V[j]):
			E[i][j]=1
			E[j][i]=1

def component(src):
	q=[src]
	comp=[0]*n
	comp[src]=1
	#unchecked=set(xrange(n))
	#unchecked.discard(src)
	while q:
		u=q.pop(0)
		for i in xrange(n):
			if E[u][i]:
				if comp[i]==comp[u]:
					return False
				if comp[i]==0:
					q.append(i)
				comp[i]=3-comp[u]
				#unchecked.discard(i)
	return comp

comp=component(0)
if not comp:
	print -1
elif comp[-1]==0:
	print 0
else:
	ratio= fractions.Fraction(V[-1].r,V[0].r)*(-1)**(comp[-1]-comp[0])
	sign = cmp(ratio.numerator,0)
	print sign*ratio.numerator,sign*ratio.denominator







