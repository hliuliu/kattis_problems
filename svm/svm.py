
import math

n=int(raw_input())

params= map(float,raw_input().split())
w,b=params[:-1],params[-1]

wnorm=sum(map(lambda x: x**2, w))
wnorm=math.sqrt(wnorm)

def dist(x):
	return (sum((i*j for i,j in zip(w,x)))+b)/wnorm


while 1:
	try:
		x=map(float,raw_input().split())
		print dist(x)
	except EOFError:
		break







