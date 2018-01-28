

mvdict={'u':(0,1),'d':(0,-1),'l':(-1,0),'r':(1,0)}


def move(tx,ty,ax,ay,dr,n,w,l):
	dx,dy=mvdict[dr]
	dx,dy=dx*n,dy*n
	tx,ty=tx+dx,ty+dy
	ax,ay=ax+dx,ay+dy
	ax=max(0,min(w-1,ax))
	ay=max(0,min(l-1,ay))
	return tx,ty,ax,ay


w,l=map(int,raw_input().split())

while w or l:
	tx,ty,ax,ay=[0]*4
	nwalks=int(raw_input())
	for _ in xrange(nwalks):
		dr,n=raw_input().split()
		n=int(n)
		tx,ty,ax,ay=move(tx,ty,ax,ay,dr,n,w,l)
	print 'Robot thinks',tx,ty
	print 'Actually at',ax,ay
	print 
	w,l=map(int,raw_input().split())





