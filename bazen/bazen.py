

from math import sqrt

def calc_diag(l):
	try:
		w=float(2*area)/l
		return w
	except:
		return 300

def calc_edge(l):
	return 250-calc_diag(l)




area=250**2//4


x,y=map(int,raw_input().split())

if (x,y)==(0,0):
	x,y=125,125
elif x==0:
	y0=y
	x=calc_diag(250-y)
	y=250-x
	if y<0:
		# x=y0*x/(y0-y)
		# y=0
		x=calc_diag(y0)
		y=0
elif y==0:
	x0=x
	y=calc_diag(250-x)
	x=250-y
	if x<0:
		# y=x0*y/(x0-x)
		# x=0
		y=calc_diag(x0)
		x=0
else:
	e=calc_edge(max(x,y))
	if x<y:
		x,y=e,0
	else:
		x,y=0,e

print '%.2f %.2f'%(x,y)



