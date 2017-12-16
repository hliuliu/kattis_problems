

def convert(from_,to,G,Gt,visited):
	start = from_
	if start==to:
		return []
	
	visited.add(start)
	for u in Gt[start]:
		if u not in visited:
			ans = convert(u,to,G,Gt,visited)
			if ans is not None:
				ans.append(Gt[start][u])
				return ans
	for u in G[start]:
		if u not in visited:
			ans = convert(u,to,G,Gt,visited)
			if ans is not None:
				ans.append(-G[start][u])
				return ans
	visited.discard(start)
	return None


def calc(seq):
	seq.sort(reverse=True)
	ans =1
	for s in seq:
		if s>0:
			ans *= s
		else:
			ans //= -s
	return ans


n =int(raw_input())

while n:
	units = raw_input().split()
	G= {u:{} for u in units}
	Gt = {u:{} for u in units}

	for _ in xrange(1,n):

		left, _, value, right = raw_input().split()
		value = int(value)
		G[right][left] = value
		Gt[left][right] = value

	

	units.sort(cmp = lambda x,y: cmp(calc(convert(x,y,G,Gt,set())), 1))
	# print units
	u = units[-1]
	toks = ['1'+units.pop()]
	while units:
		toks.append('%d%s'%(calc(convert(u, units[-1], G,Gt, set())),units.pop()))
	print ' = '.join(toks)


	n = int(raw_input())





