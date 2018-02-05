

board = [raw_input() for _ in xrange(5)]


knights = []


def valid(i,j):
	xi,yi = knights[i]
	xj,yj = knights[j]
	return set([abs(xj-xi),abs(yj-yi)]) != {1,2}

for i in xrange(5):
	for j in xrange(5):
		if board[i][j]=='k':
			knights.append((i,j))


if len(knights)!=9:
	print 'invalid'
else:
	for i in xrange(len(knights)):
		for j in xrange(i):
			if not valid(i,j):
				print 'invalid'
				break
		else:
			continue
		break
	else:
		print 'valid'



