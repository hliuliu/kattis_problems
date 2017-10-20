

n,s = map(int,raw_input().split())

pts = []

for _ in xrange(n):
	x,y = map(int, raw_input().split())
	key = 0
	elem = (x,y)
	for j in xrange(32):
		x<<=1
		y<<=1
		key<<=2
		if y>s:
			y-=s
			if x>s:
				key+=2
				x-=s
			else:
				key +=1
		else:
			x,y = y,x
			if y>s:
				key+=3
				x=s-x
				y=(s<<1)-y
	pts.append((key,elem))





pts.sort()

for key,(x,y) in pts:
	print x,y

