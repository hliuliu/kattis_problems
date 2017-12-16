

shift_keyboard=[
'QWERTYUIOP','ASDFGHJKL:','ZXCVBNM<>?','**______**'
]

normal_keyboard=[
'qwertyuiop','asdfghjkl;','zxcvbnm,./','**______**'
]

moves={(i,j) for i in [1,-1] for j in [2,-2]}
moves.update({(j,i) for i,j in moves})
#print moves

def inbound(x,y):
	try:
		normal_keyboard[x][y]
		return True
	except:
		return False

def char_typed(s1,s2,moved):
	# moved= 1 if knight2 moved , 0 if knight1 moved
	if moved:# knight 2 moved 
		s1,s2=s2,s1
	if normal_keyboard[s1[0]][s1[1]]=='*':
		return ''
	if normal_keyboard[s1[0]][s1[1]]=='_':
		return ' '
	if normal_keyboard[s2[0]][s2[1]]=='*':
		return shift_keyboard[s1[0]][s1[1]]
	return normal_keyboard[s1[0]][s1[1]]

'''
def cantype(line,s1,s2):
	if not line:
		return True
	x,y=s1
	for dx,dy in moves:
		nx,ny=x+dx,y+dy
		if inbound(nx,ny) and (nx,ny)!=s2:
			c=char_typed((nx,ny),s2,0)
			if not c:
				res=cantype(line,(nx,ny),s2)
				#print res,line
				if res:
					return True
			elif c==line[0]:
				#print 'ok'
				line.pop(0)
				res=cantype(line,(nx,ny),s2)
				if res:
					return True
				line.insert(0,c)
	x,y=s2
	for dx,dy in moves:
		nx,ny=x+dx,y+dy
		if inbound(nx,ny) and (nx,ny)!=s1:
			c=char_typed((nx,ny),s1,0)
			if not c:
				res=cantype(line,(nx,ny),s1)
				if res:
					return True
			elif c==line[0]:
				line.pop(0)
				res=cantype(line,(nx,ny),s1)
				if res:
					return True
				line.insert(0,c)
	return False
''' # brutal failure?


def hash_state(s1,s2):
	if s1<s2:
		s1,s2=s2,s1
	h=0
	x,y=s1
	h+=10*x+y
	h*=40
	x,y=s2
	h+=10*x+y
	return h

def hash_state_with_size(s1,s2,n,h=None):
	if h==None:
		h=hash_state(s1,s2)
	return h*101+n


def valid_neighbours(s):
	x,y=s
	for dx,dy in moves:
		nx,ny=x+dx,y+dy
		if inbound(nx,ny):
			yield (nx,ny)

def get_next_states(s1,s2,h,output_len,line):
	states=[]
	n=output_len[h]
	for ns1 in valid_neighbours(s1):
		if ns1==s2:
			continue
		c=char_typed(ns1,s2,0)
		nh=hash_state(ns1,s2)
		if not c:
			states.append((ns1,s2))
			if output_len[nh]<n:
				output_len[nh]=n
		elif line[n]==c:
			states.append((ns1,s2))
			if output_len[nh]<n+1:
				output_len[nh]=n+1
	for ns2 in valid_neighbours(s2):
		if s1==ns2:
			continue
		c=char_typed(s1,ns2,1)
		nh=hash_state(s1,ns2)
		if not c:
			states.append((s1,ns2))
			if output_len[nh]<n:
				output_len[nh]=n
		elif line[n]==c:
			states.append((s1,ns2))
			if output_len[nh]<n+1:
				output_len[nh]=n+1
	return states

def cantype(line,s1,s2):
	q=[]
	output_len=[0]*1600
	visited=set()
	q.append((s1,s2))
	visited.add(hash_state_with_size(s1,s2,0))
	while q:
		s1,s2=q.pop(0)
		h=hash_state(s1,s2)
		if output_len[h]==len(line):
			return True
		nbrs=get_next_states(s1,s2,h,output_len,line)
		for ns1,ns2 in nbrs:
			nh=hash_state(ns1,ns2)
			nhs=hash_state_with_size(ns1,ns2,
				output_len[nh],nh
				)
			if nhs not in visited:
				q.append((ns1,ns2))
				visited.add(nhs)
	return False





initial_states=[(3,0),(3,9)]

line= raw_input()#.strip()
#print len(line)
while line!='*':
	s1,s2=initial_states
	line=list(line)
	print int(cantype(line,s1,s2))
	line=raw_input()#.strip()






