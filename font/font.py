
bits=[1]

for _  in xrange(26):
	bits.append(bits[-1]<<1)

binv={j:i for i,j in enumerate(bits)}

def hash_word(word):
	m=0
	for c in word:
		m|=(bits[(ord(c)-ord('a'))])
	return m

n=int(raw_input())

masks=[hash_word(raw_input()) for _ in xrange(n)]

target=(bits[26])-1

nb=[0]*bits[n]

for i in xrange(1,bits[n]):
	x=i&-i
	nb[i]=(nb[i^x]|masks[binv[x]])

print nb.count(target)




