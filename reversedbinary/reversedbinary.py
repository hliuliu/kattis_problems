


n=int(raw_input())

rev=0

while n:
	rev<<=1
	rev^=(n&1)
	n>>=1

print rev



