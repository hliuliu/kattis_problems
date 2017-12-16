


moves = [(1,0),(-1,0),(0,1),(0,-1)]


def inbound(i,j,n,m):
	return 0<=i<n and 0<=j<m


def nbrs(i,j,n,m):
	for dx,dy in moves:
		if inbound(i+dx,j+dy,n,m):
			yield (i+dx, j+dy)


def done():
	return all(['T' not in row for row in grid])


n,m = map(int,raw_input().split())

grid = [list(raw_input()) for _ in xrange(n)]

for i in xrange(n):
	for j in xrange(m):
		if grid[i][j] == '.':
			grid[i][j] =0

for i in [0,-1]:
	for j in xrange(m):
		if grid[i][j]=='T':
			grid[i][j] = 1

for i in xrange(1,n-1):
	for j in [0,-1]:
		if grid[i][j]=='T':
			grid[i][j] = 1



remaining = {(i,j) for i in xrange(n) for j in xrange(m) if grid[i][j]=='T'}

discard = set()
for i,j in remaining:
	for x,y in nbrs(i,j,n,m):
		if grid[x][y] == 0:
			grid[i][j] =1
			discard.add((i,j))

for el in discard:
	remaining.discard(el)

layer = 2
while remaining:
	discard = set()
	for i,j in remaining:
		for x,y in nbrs(i,j,n,m):
			if grid[x][y]!='T':
				discard.add((i,j))
				break
	for i,j in discard:
		grid[i][j] = layer
		remaining.discard((i,j))
	layer +=1






maxnr = max(map(max, grid))

numch = 2 if maxnr<10 else 3

pad = lambda x: '.'*numch if x==0 else '.'*(numch-1)+str(x) if x<10 else '.'*(numch-2)+str(x)

for row in grid:
	print ''.join(map(pad, row))


