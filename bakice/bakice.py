



r,c=map(int,raw_input().split())


tram=[raw_input() for _ in xrange(r)]


def hashcoords(x,y):
	return 100*x+y

def unhashcoords(h):
	return h//100,h%100

def distsq(x1,y1,x2,y2):
	return (x1-x2)**2+(y1-y2)**2

def hashed_distsq(h1,h2):
	return distsq(*(unhashcoords(h1)+unhashcoords(h2)))

passengers=set()
seats=set()

for i in xrange(r):
	for j in xrange(c):
		if tram[i][j]=='X':
			passengers.add(hashcoords(i,j))
		elif tram[i][j]=='L':
			seats.add(hashcoords(i,j))

closest_seat={}


for p in passengers:
	closest_seat[p]=sorted(seats,key=lambda x: hashed_distsq(p,x))

# closest_passenger_dist={}

# for s in seats:
# 	closest_passenger_dist[s]=min([hashed_distsq(p,s) for p in passengers])

closest_passengers={s:{} for s in seats}

for s in seats:
	for p in passengers:
		d=hashed_distsq(p,s)
		closest_passengers[s][d]=closest_passengers[s].get(d,set())
		closest_passengers[s][d].add(p)
	closest_passengers[s]=map(lambda x: closest_passengers[s][x],sorted(closest_passengers[s]))


closest_seat_rank={p:{j:i for i,j in enumerate(closest_seat[p])} for p in passengers}

attack={}

while closest_passengers:
	used={}
	for s in closest_passengers:
		for pl in closest_passengers[s]:
			found=False
			for p in pl:
				if p in attack:
					continue
				if p not in used:
					used[p]=s
				elif closest_seat_rank[p][s]<closest_seat_rank[p][used[p]]:
					used[p]=s
				found=True
			if found:
				break
	if not used:
		break
	for p in used:
		if used[p] in closest_passengers:
			del closest_passengers[used[p]]
	attack.update(used)


target={s:0 for s in seats}

for p in attack:
	target[attack[p]]+=1

count=0
for s,ns in target.iteritems():
	if ns>1:
		count+=1

print count




