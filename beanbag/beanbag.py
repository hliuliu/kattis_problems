

def unmask(h,b):
	vs=[]
	for _ in xrange(b):
		vs.insert(0,h%101)
		h//=101
	return vs

def mask(vs):
	h=0
	for v in vs:
		h*=101
		h+=v
	return h

cache={}

def optimize(vs,farms,sm):
	h= mask(vs)
	if h in cache:
		return cache[h]
	ans=sm
	for farm in farms:
		m = min([vs[bean] for bean in farm])
		if m>0:
			term=0
			for bean in farm:
				if vs[bean]==m:
					vs[bean]-=1
					#print vs,
					term=max(term,optimize(vs,farms,sm-1))
					vs[bean]+=1
			ans=min(ans,term)
	cache[h]=ans
	return ans




b=int(raw_input())

vs=[0]+map(int,raw_input().split())

t=int(raw_input())

farms=[]

for _ in xrange(t):
	farms.append(map(int,raw_input().split())[1:])

print optimize(vs,farms,sum(vs))

