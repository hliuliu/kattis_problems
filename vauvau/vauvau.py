

a,b,c,d = map(int,raw_input().split())


p,m,g = map(int,raw_input().split())


def calc(t,a,b):
	t %= (a+b)
	if t==0 or t>a:
		return 0
	return 1


def get_word(n):
	if n==0:
		return 'none'
	if n==1:
		return 'one'
	return 'both'

for t in [p,m,g]:
	print get_word (calc(t,a,b)+calc(t,c,d))



