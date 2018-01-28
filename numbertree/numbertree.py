

h,seq=(raw_input().split()+[''])[:2]

h=int(h)

factor=1

node=(1<<(h+1))

for c in seq:
	factor<<=1
	if c=='R':
		factor+=1


print node-factor

