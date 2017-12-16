
mdir={(0,1),(1,0)}

def inbound(m,x,y):
	return 0<=x<3 and 0<=y<m


def nextcoords(m,x,y):
	if y==m-1:
		return x+1,0
	return x, y+1


def count_trays(shelf,m,x,y):
	while inbound(m,x,y) and shelf[x]&bits[y]:
		x,y=nextcoords(m,x,y)
	if not inbound(m,x,y):
		return 1
	# if (x,y)==(2,m-1):
	# 	return 1
	ans=0
	shelf[x]|=bits[y]
	xnext,ynext=nextcoords(m,x,y)
	ans+=count_trays(shelf,m,xnext,ynext)
	for dx,dy in mdir:
		if not inbound(m,x+dx,y+dy):
			continue
		if not shelf[x+dx]&bits[y+dy]:
			shelf[x+dx]|=bits[y+dy]
			ans+=count_trays(shelf,m,xnext,ynext)
			shelf[x+dx]^=bits[y+dy]
	#print x,y,ans
	shelf[x]^=bits[y]
	return ans




m,n = map(int,raw_input().split())

shelf = [0 for _ in xrange(3)]

bits=[1]
for i in xrange(1,25):
	bits.append(bits[-1]<<1)

if n:
	leaks=map(float, raw_input().split())
	while leaks:
		y,x=leaks[:2]
		leaks[:2]=[]
		shelf[int(x)]|=1<<(int(y))

print count_trays(shelf,m,0,0)




