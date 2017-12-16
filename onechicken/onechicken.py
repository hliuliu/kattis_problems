

n,m=map(int,raw_input().split())

if n>m:
	print 'Dr. Chaz needs %d more piece%s of chicken!'%(n-m,'' if n-m==1 else 's')
else:
	print 'Dr. Chaz will have %d piece%s of chicken left over!'%(m-n, '' if m-n==1 else 's')

