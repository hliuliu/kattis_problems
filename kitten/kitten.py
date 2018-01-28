

branches=range(101)

k=int(raw_input())

conn=map(int,raw_input().split())

while conn!=[-1]:
	r=conn.pop(0)
	for c in conn:
		branches[c]=r
	conn=map(int,raw_input().split())


while branches[k]!=k:
	print k,
	k=branches[k]
print k



