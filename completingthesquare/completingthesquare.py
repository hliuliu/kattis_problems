
def midpt2(p1,p2):
	x1,y1=p1
	x2,y2=p2
	return (x1+x2),(y1+y2)



def distsq(p1,p2):
	x1,y1=p1
	x2,y2=p2
	return (x2-x1)**2+(y2-y1)**2

p1,p2,p3 = [map(int,raw_input().split()) for _ in xrange(3)]

d12= distsq(p1,p2)
d13= distsq(p1,p3)
d23= distsq(p2,p3)

if d12==d13:
	p1,p3=p3,p1
elif d12==d23:
	p2,p3=p3,p2

mx,my= midpt2(p1,p2)

x3,y3= p3

ox,oy = mx-x3, my-y3

print ox,oy




