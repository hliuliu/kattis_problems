

secret=1


moves={'A':(1,2),'B':(2,3),'C':(1,3)}

seq=raw_input().strip()

for c in seq:
	a,b = moves[c]
	if secret==a:
		secret=b
	elif secret==b:
		secret=a

print secret







