

peg = [raw_input() for _ in xrange(7)]

ct =0

for i in xrange(7):
	for j in xrange(7):
		if peg[i][j]=='.':
			if i>=2 and peg[i-1][j]=='o' and peg[i-2][j]=='o':
				ct+=1
			if i<5 and peg[i+1][j]=='o' and peg[i+2][j]=='o':
				ct+=1
			if j>=2 and peg[i][j-2:j]=='oo':
				ct+=1
			if j<5 and peg[i][j+1:j+3]=='oo':
				ct+=1

print ct


