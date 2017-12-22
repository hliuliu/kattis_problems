
from math import sqrt

def ceil(x):
	if x==int(x):
		return int(x)
	return int(x)+1

n=int(raw_input())

def rotgrid(grid):
	m=len(grid)
	for i in xrange(m):
		for j in range(i+1,m):
			grid[i][j],grid[j][i]=grid[j][i],grid[i][j]
	for i in grid:
		i.reverse()



for i in xrange(n):
	msg=raw_input().strip()
	l=len(msg)
	m=ceil(sqrt(l))
	#print l,m
	grid=[[0]*m for j in xrange(m)]
	for pos in xrange(m*m):
		if pos <l:
			grid[pos/m][pos%m]=msg[pos]
		else:
			grid[pos/m][pos%m]='*'
	#print grid
	
	rotgrid(grid)
	output=''
	for i in grid:
		output+=''.join(i).replace('*','')
	print output