


n,t= map(int,raw_input().split())

bank_line=[[] for _ in xrange(t)]

for _ in xrange(n):
	ci,ti=map(int,raw_input().split())
	bank_line[ti].append(ci)

'''
def getmax(bank_line):
	opt=0
	delta=0
	x,y=-1,-1
	while opt==0 and delta<len(bank_line):
		for i in xrange(delta,len(bank_line)):
			try:
				#opt=max(opt,bank_line[i][i-delta])
				if bank_line[i][i-delta]>opt:
					opt=bank_line[i][i-delta]
					x,y=i,i-delta
			except IndexError:
				pass
		delta+=1
	if x>=0:
		del bank_line[x][y]
	return opt
'''

num=1
for l in bank_line:
	l.sort(reverse=True)
	l[:]=l[:num]
	num+=1




def calc(t):
	sols=[0]*t
	for i in xrange(t):
		if bank_line[i]:
			sols[i]=bank_line[i][0]
		for j in xrange(1,len(bank_line[i])):
			minind,minval=-1,bank_line[i][j]
			for k in xrange(i):
				if sols[k]<minval:
					minind,minval=k,sols[k]
			if minind>=0:
				sols[minind]=bank_line[i][j]
	return sum(sols)




amount=calc(t)

print amount








