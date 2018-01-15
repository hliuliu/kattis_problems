

def sum_digits(m):
	return sum(map(int,str(m)))



n=int(raw_input())

while n:
	val=n*10
	sd=sum_digits(n)
	for i in xrange(11,101):
		val+=n
		if sum_digits(val)==sd:
			print i
			break
	n=int(raw_input())










