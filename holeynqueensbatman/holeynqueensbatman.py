

def inbounds(x,y,n):
	return all((0<=i<n for i in [x,y]))



diags={(-1,1),(-1,-1)}

cache={}

def valid(board,row,col,occ):
	n=len(board)
	if not board[row][col]:
		return False
	#if (row,col) in cache:
	#	return cache[(row,col)]>=row
	for x,y in enumerate(occ):
		if x+y==row+col or x-y==row-col:
			#cache[(row,col)]=(x,y)
			return False
	#cache[(row,col)]=(row,-1)
	return True

	




def numsols(board,row,unused,occ=[]):
	if row==len(board):
		return 1
	nsol=0
	for i in xrange((len(board))):
		if unused[i] and valid(board,row,i,occ):
			occ.append(i)
			unused[i]=0
			nsol+=numsols(board,row+1,unused,occ)
			occ.pop()
			try:
				unused[i]=1
			except:
				print i,len(board),len(unused)
				exit()
	return nsol







n,m=map(int,raw_input().split())


while m or n:
	board=[[1]*n for _ in xrange(n)]
	for _ in xrange(m):
		x,y=map(int,raw_input().split())
		board[x][y]=0
	print numsols(board,0,[1]*n)
	cache={}
	n,m=map(int,raw_input().split())



