


state=[map(int,raw_input().split()) for _ in xrange(4)]

move=int(raw_input())

def rotccw():
	global state
	state[0][0],state[3][0],state[3][3],state[0][3]=state[0][3],state[0][0],state[3][0],state[3][3]
	state[0][1],state[2][0],state[3][2],state[1][3]=state[1][3],state[0][1],state[2][0],state[3][2]
	state[0][2],state[1][0],state[3][1],state[2][3]=state[2][3],state[0][2],state[1][0],state[3][1]
	state[1][1],state[2][1],state[2][2],state[1][2]=state[1][2],state[1][1],state[2][1],state[2][2]


for i in  xrange(move):
	rotccw()

for row in state:
	nz=0
	while 0 in row:
		row.remove(0)
		nz+=1
	i=0
	while i+1<len(row):
		if row[i]==row[i+1]:
			row[i]<<=1
			del row[i+1]
			nz+=1
		i+=1
	row.extend([0]*nz)



for i in xrange((4-move)%4):
	rotccw()

for row in state:
	print ' '.join(map(str,row))


