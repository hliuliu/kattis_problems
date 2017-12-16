

from math import sqrt

root2=sqrt(2)

needed=2

raw_input()

amounts= map(int,raw_input().strip().split())


def tape_length(amounts,needed,l,w):
	# l>w
	if not amounts:
		if needed<=0:
			return 0
		return 'impossible'
	numitems=amounts.pop(0)
	tl=l*(needed>>1)
	needed-=numitems
	if needed<=0:
		return tl
	needed<<=1
	l,w=w,w/root2
	res=tape_length(amounts,needed,l,w)
	if type(res)!=str:
		return tl+res
	return res




fourth2=sqrt(root2)

print tape_length(amounts,needed,1.0/fourth2/root2,1.0/fourth2/root2/root2)

