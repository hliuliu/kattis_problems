

mod = 10**9+7

n,k = map(int,raw_input().split())

codetree = {}

def insert(code,index):
	posn = codetree
	for c in code:
		if c not in posn:
			posn[c] = {}
		posn = posn[c]
	posn[None] = index


codes = sorted([raw_input() for _ in xrange(n)])

for i in xrange(n):
	insert(codes[i], i)

teststr = raw_input()

def construct(test):
	seq = []
	posn = codetree
	for c in test:
		posn = posn[c]
		if  None in posn:
			seq.append(posn[None])
			posn = codetree
	return seq

seq = construct(teststr)


def perm(n,k):
	n%=mod
	ans = 1
	for _ in xrange(k):
		ans *= n
		ans %= mod
		n-=1
	return ans%mod


def count_inversions(seq, start, end, inv, rseq):
	if end-start<=1:
		return

	mid = (start+end)>>1
	count_inversions(seq,start,mid,inv, rseq)
	count_inversions(seq,mid,end,inv, rseq)
	i = start
	j = mid
	tmp = []
	while i<mid and j<end:
		if seq[j]<seq[i]:
			tmp.append(seq[j])
			inv[rseq[seq[j]]] += mid - i
			j+=1
		else:
			tmp.append(seq[i])
			i += 1
	while i<mid:
		tmp.append(seq[i])
		i+=1
	seq[start:j] = tmp



def rank(seq):
	#discard = set()
	#print seq
	pos = -1
	ans = 0
	pnums = [1]
	for i in xrange(1,k):
		pnums.insert(0, (((n-k+i)%mod)*(pnums[0]))%mod )
	inv = [0]*k
	count_inversions(list(seq), 0, k, inv, {j:i for i,j in enumerate(seq)})
	#print inv
	for i,x in enumerate(seq):
		pos += 1
		ans += pnums[pos]*(x+inv[i]-i)
		ans %= mod
		#discard.add(x)
	return ans


#print seq
print (rank(seq)+1)%mod

