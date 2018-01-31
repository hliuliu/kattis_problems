

state=[False]*2



def simulate(n):
	for _ in xrange(7):
		state[n&1]=not state[n&1]
		n>>=1


while 1:
	state=[False]*2
	try:
		line=raw_input()
		for c in line:
			simulate(ord(c))
		if True in state:
			print 'trapped'
		else:
			print 'free'
	except EOFError:
		break


