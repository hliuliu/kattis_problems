



n=int(raw_input())

while n:
	bits=['?']*32
	for _ in xrange(n):
		inst=raw_input().split()
		if inst[0]=='CLEAR':
			i=int(inst[1])
			bits[i]='0'
		elif inst[0]=='SET':
			i=int(inst[1])
			bits[i]='1'
		else:
			i,j=map(int,inst[1:])
			if inst[0]=='AND':
				if bits[j]=='0':
					bits[i]='0'
				elif bits[j]=='?' and bits[i]!='0':
					bits[i]='?'
			else:
				if bits[j]=='1':
					bits[i]='1'
				elif bits[j]=='?' and bits[i]!='1':
					bits[i]='?'
	print ''.join(reversed(bits))
	n=int(raw_input())


