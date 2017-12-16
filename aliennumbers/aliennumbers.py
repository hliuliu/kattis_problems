



def word_to_int(word,src):
 	k=len(src)
 	x=0
 	sd={j:i for i,j in enumerate(src)}
 	for w in word:
 		x=x*k+sd[w]
 	return x

def int_to_word(num,target):
	k=len(target)
	s=''
	while num:
		s=target[num%k]+s
		num=num//k
	return s




n=int(raw_input())

for i in xrange(1,n+1):
	word,src,target=raw_input().split()
	num=word_to_int(word,src)
	print 'Case #%d: %s'%(i,int_to_word(num,target))




