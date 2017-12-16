

def binom(n,r):
	if r>n-r:
		r=n-r
	prod=1
	for i in xrange(1,r+1):
		prod*=n-i+1
		prod//=i
	return prod




def multinomial(n,vals):
	prod=1
	for v in vals:
		prod*=binom(n,v)
		n-=v
	return prod





def num_anagrams(word,n):
	cnts={}
	for c in word:
		cnts[c]=cnts.get(c,0)+1
	return multinomial(n,cnts.values())




while 1:
	try:
		word=raw_input()
		n=len(word)
		print num_anagrams(word,n)
	except EOFError:
		break






