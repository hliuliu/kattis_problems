
import sys


def create_array(*args):
	if not len(args):
		return -1
	A=[]
	args1=args[1:]
	for i in xrange(args[0]):
		A.append(create_array(*args1))
	return A

numcases=int(raw_input())


def func(k,i,j,table):
	if i>j:
		return 0
	if table[k][i][j]>=0:
		return table[k][i][j]
	if k ==1:
		table[k][i][j]=j*(j+1)/2-i*(i-1)/2
		return table[k][i][j]
	minval=sys.maxint
	for s in xrange(i,j+1):
		minval=min(minval,s+max(func(k-1,i,s-1,table),func(k,s+1,j,table)))
	table[k][i][j]=minval
	return minval



def optimal_sol(k,m,table):
	return func(k,1,m,table)
	#return min((func(k,m,t,table) for t in xrange(m,0,-1)))



for i in xrange(numcases):
	k,m=map(int,raw_input().strip().split())
	table= create_array(k+1,m+1,m+1)
	print optimal_sol(k,m,table)
