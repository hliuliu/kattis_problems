

_,code,guess=raw_input().split()

r=0

code_counts={}
guess_counts={}

for i,j in zip(code,guess):
	if i==j:
		r+=1
	else:
		code_counts[i]=code_counts.get(i,0)+1
		guess_counts[j]=guess_counts.get(j,0)+1

s=0

for c in code_counts:
	s+=min(code_counts[c],guess_counts.get(c,0))

print r,s



