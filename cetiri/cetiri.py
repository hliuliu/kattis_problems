

l=map(int,raw_input().split())

l.sort()

a,b,c=l

if b-a<c-b:
	print b*2-a
elif b-a>c-b:
	print a+c-b
else:
	print c*2-b





