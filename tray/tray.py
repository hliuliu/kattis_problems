
mdir={(0,1),(1,0)}

def inbound(m,x,y):
	return (x,y) in ibs


def nextcoords(m,x,y):
	if y==m-1:
		return x+1,0
	return x, y+1


cache={}

def count_trays(shelf,m,x,y):
	if (shelf,x,y) in cache:
		return cache[(shelf,x,y)]
	while inbound(m,x,y) and shelf&bits[getbitpos(m,x,y)]:
		x,y=nextcoords(m,x,y)
		#cache[(shelf,x,y)]=count_trays(shelf,m,xnext,ynext)
		#return cache[(shelf,x,y)]	
	if not inbound(m,x,y):
		return 1
	# if (x,y)==(2,m-1):
	# 	return 1
	ans=0
	shelf|=bits[getbitpos(m,x,y)]
	xnext,ynext=nextcoords(m,x,y)
	ans+=count_trays(shelf,m,xnext,ynext)
	for dx,dy in mdir:
		pos=getbitpos(m,x+dx,y+dy)
		if not inbound(m,x+dx,y+dy):
			continue
		if not shelf&bits[pos]:
			shelf|=bits[pos]
			#if dy==1:
			#	xnext,ynext=nextcoords(m,xnext,ynext)
			ans+=count_trays(shelf,m,xnext,ynext)
			shelf^=bits[pos]
	#print x,y,ans
	shelf^=bits[getbitpos(m,x,y)]
	cache[(shelf,x,y)]=ans
	return ans

def getbitpos(m,x,y):
	return m*x+y


m,n = map(int,raw_input().split())

shelf = 0

bits=[1]
for i in xrange(1,73):
	bits.append(bits[-1]<<1)

if n:
	leaks=map(float, raw_input().split())
	while leaks:
		y,x=leaks[:2]
		leaks[:2]=[]
		shelf|=bits[getbitpos(m,int(x),int(y))]

ibs={(i,j) for i in xrange(3) for j in xrange(m)}

print count_trays(shelf,m,0,0)




