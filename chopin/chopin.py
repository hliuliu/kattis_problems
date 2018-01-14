
num=0


def up(letter):
	if letter=='G':
		return 'A'
	return chr(ord(letter)+1)

def down(letter):
	if letter=='A':
		return 'G'
	return chr(ord(letter)-1)


while 1:
	try:
		note,tone=raw_input().split()
		num+=1
		alt=None
		if note[-1]=='#':
			alt=up(note[0])+'b'
		elif note[-1]=='b':
			alt=down(note[0])+'#'
		print 'Case %d:'%num, (alt+' '+tone if alt else 'UNIQUE')
	except EOFError:
		break

