

def sum_digits(n):
	ans=0
	while n:
		n,r=divmod(n,10)
		ans+=r
	return ans
	# if not n:
	# 	return 0
	# d,r=divmod(n)
	# return r+sum_digits(d)



l,d,x=[int(raw_input()) for _ in xrange(3)]

while sum_digits(l)!=x:
	l+=1

print l

while sum_digits(d)!=x:
	d-=1

print d
