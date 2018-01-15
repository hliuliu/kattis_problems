
def kb_update(ld,s):
	for i in xrange(len(s)-1):
		ld[s[i+1]]=s[i]

def dupchar(s):
	return ''.join((c*2 for c in s))

ld={}

for s in ['11234567890-=','QWERTYUIOP[]\\','ASDFGHJKL;\'','ZXCVBNM,./','  ']:
	kb_update(ld,s)


while 1:
	try:

		line = raw_input()

		print ''.join(map(lambda x: ld[x],line))
	except EOFError:
		break


