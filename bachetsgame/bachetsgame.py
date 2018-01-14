


seq=map(int,raw_input().split())

while seq:
	n,m=[seq.pop(0) for _ in [0,0]]
	seq.sort()
	wins=[False]
	i=1
	while i<=n:
		for s in seq:
			if s>i:
				wins.append(False)
				break
			if not wins[i-s]:
				wins.append(True)
				break
		else:
			wins.append(False)
		i+=1
	if wins[-1]:
		print 'Stan wins'
	else:
		print 'Ollie wins'

	seq=map(int,raw_input().split())


