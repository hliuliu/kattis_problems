cn=1

while 1:
	try:
		
		n=int(raw_input())
		A=[int(raw_input()) for _ in xrange(n)]
		#sms=(A[i]+A[j] for i in xrange(n) for j in xrange(i+1,n))

		m=int(raw_input())
		print 'Case %d:'%cn

		for k in xrange(m):
			q=int(raw_input())
			v=A[0]+A[1]
			for i in xrange(n):
				for j in xrange(i+1,n):
					nv=A[i]+A[j]
					if abs(nv-q)<abs(v-q):
						v=nv
			print 'Closest sum to %d is %d.'%(q,v)
		cn+=1
	except EOFError:
		break




