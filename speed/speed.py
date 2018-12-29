
from __future__ import division


n,t = map(int,raw_input().split())

dists = []
spread = []

for _ in xrange(n):
	d,s = map(int,raw_input().split())
	dists.append(d)
	spread.append(s)


def f(c):
	return sum([d/(s+c) for d,s in zip(dists,spread)])-t

def fder(c):
	return -sum([d/(s+c)**2 for d,s in zip(dists,spread)])

eps = 1e-8

clow = -min(spread)
chi = 1000000
while f(chi)>0:
	chi*=2

for _ in [0]*200:
	cmid = (clow+chi)/2
	sol = f(cmid)
	if abs(sol)<eps:
		print cmid
		break
	if sol>0:
		clow = cmid
	else:
		chi = cmid
else:
	print cmid







