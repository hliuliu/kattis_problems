


r,c = map(int,raw_input().split())

puzzle = [raw_input() for _ in xrange(r)]

smw = 'z'*100

def findh(i,j):
	jj = j+1
	w = puzzle[i][j]
	while jj<c and puzzle[i][jj]!='#':
		jj+=1
		w+=puzzle[i][jj-1]
	return w

def findv(i,j):
	ii = i+1
	w = puzzle[i][j]
	while ii<r and puzzle[ii][j]!='#':
		ii+=1
		w+=puzzle[ii-1][j]
	return w


for i in xrange(r):
	for j in xrange(c):
		if puzzle[i][j]=='#':
			continue
		if j==0 or puzzle[i][j-1]=='#':
			word =findh(i,j)
			if len(word)>1:
				smw = min(word, smw)
		if i==0 or puzzle[i-1][j]=='#':
			word = findv(i,j)
			if len(word)>1:
				smw = min(word, smw)


print smw


