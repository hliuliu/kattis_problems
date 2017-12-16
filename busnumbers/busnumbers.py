

n= int(raw_input())

busses = map(int,raw_input().split())

busses.sort()

i=0
toks=[]
while i<n:
	start = busses[i]
	end = start
	i+=1
	while i<n and end+1==busses[i]:
		end+=1
		i+=1
	if end==start:
		toks.append(str(end))
	elif end-start==1:
		toks.extend(map(str,[start,end]))
	else:
		toks.append('%s-%s'%(start,end))

print ' '.join(toks)

