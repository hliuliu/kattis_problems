


subs='welcome to code jam'


def create_table(msg,subs):
	return [[-1]*(len(subs)+1) for i in xrange(len(msg)+1)]


def numocc(msg,subs,table):
	if table[len(msg)][len(subs)]>=0:
		return table[len(msg)][len(subs)]
	if len(subs)==1:
		table[len(msg)][len(subs)]=msg.count(subs[0])
		return table[len(msg)][len(subs)]
	if len(msg)<len(subs):
		table[len(msg)][len(subs)]=0
		return 0
	last=subs[-1]
	ml=msg.pop()
	ans=numocc(msg,subs,table)
	if ml==last:
		subs.pop()
		ans+=numocc(msg,subs,table)
		subs.append(last)
	msg.append(ml)
	table[len(msg)][len(subs)]=ans
	return ans



n=int(raw_input())

for i in xrange(1,n+1):
	msg=raw_input()
	table=create_table(msg,subs)
	print 'Case #%d: %04d'%(i,numocc(list(msg),list(subs),table))


