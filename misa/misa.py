

dirs={(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)}


r,s=map(int,raw_input().split())



def bound(a,b):
	return 0<=a<r and 0<=b<s


def compute(seating):
	humans=[[0]*s for _ in xrange(r)]
	for i in xrange(r):
		for j in xrange(s):
			if seating[i][j]=='o':
				for dx,dy in dirs:
					if bound(i+dx,j+dy):
						humans[i+dx][j+dy]+=1
	return humans

def entries(seating,A):
	for srow,row in zip(seating,A):
		for sel,el in zip(srow,row):
			if sel=='.':
				yield el



def argmax(seating,A,m):
	for i in xrange(r):
		for j in xrange(s):
			if seating[i][j]=='.' and A[i][j]==m:
				return i,j


seating=[list(raw_input()) for _ in xrange(r)]


nbrs=compute(seating)


try:
	m=max(entries(seating,nbrs))
	mx,my=argmax(seating,nbrs,m)
	seating[mx][my]='o'
	#print mx,my

	for dx,dy in dirs:
		if bound(mx+dx,my+dy):
			nbrs[mx+dx][my+dy]+=1
	#print nbrs,seating
except:
	 pass



v=0
for i in xrange(r):
	for j in xrange(s):
		if seating[i][j]=='o':
			v+=nbrs[i][j]



print v//2



