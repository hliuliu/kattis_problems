

n,t=map(int,raw_input().split())

tasks=map(int,raw_input().split())

s=0
num=0
for i in tasks:
	if s+i>t:
		break
	s+=i
	num+=1
print num



