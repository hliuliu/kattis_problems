


orientations=[
	[],
	['0','0000'],
	['00'],
	['10','001'],
	['01','100'],
	['000','10','01','101'],
	['00','000','20','011'],
]

orientations.append(map(lambda x: ''.join(reversed(x)),orientations[-1]))


def numways(c,heights,p):
	pc=orientations[p]
	count=0
	pc=map(lambda s: map(int,s),pc)
	#print pc
	for ori in pc:
		for i in xrange(c-len(ori)+1):
			if len(set([k-h for h,k in zip(heights[i:i+len(ori)],ori)]))==1:
				#print i,ori
				count+=1
	return count




c,p=map(int,raw_input().split())

heights=map(int,raw_input().split())

print numways(c,heights,p)


