

board=[[0]*8 for _ in xrange(8)]

def readBoard():
	counter =0;
	while counter<17:
		rowstr=raw_input()
		if counter&1:
			rownum = (counter-1)>>1
			rowlist=rowstr.split('|')[1:-1]
			for col,entry in enumerate(rowlist):
				board[rownum][col]=entry[1]
		counter+=1

readBoard()

white={}
for c in 'KQRBNP':
	white[c]=[]

black={}
for c in 'kqrbnp':
	black[c]=[]

def white_key(pos):
	x,y=pos
	return int(y),x

def black_key(pos):
	x,y=pos
	return -int(y),x


for i,row in enumerate(board):
	for j,col in enumerate(row):
		if col in white:
			white[col].append(chr(ord('a')+j)+str(8-i))
		elif col in black:
			black[col].append(chr(ord('a')+j)+str(8-i))

print 'White:',

wl=[]
for c in 'KQRBNP':
	extra = (c if c!='P' else '')
	white[c].sort(key=white_key)
	for pos in white[c]:
		wl.append(extra+pos)
print ','.join(wl)

print 'Black:',

bl=[]
for c in 'kqrbnp':
	extra = (c.upper() if c!='p' else '')
	black[c].sort(key=black_key)
	for pos in black[c]:
		bl.append(extra+pos)
print ','.join(bl)




