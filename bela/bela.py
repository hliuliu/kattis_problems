

dom=[11,4,3,20,10,14,0,0]
ndom=[11,4,3,2,10,0,0,0]

nums='AKQJT987'

table= {i:[j,k] for i,j,k in zip(nums,ndom,dom)}


n,domsuit=raw_input().strip().split()
n=int(n)


s=0

for i in xrange(n*4):
	num,suit=raw_input().strip()
	s+=table[num][int(suit==domsuit)]

print s


