

while 1:
	try:
		line=raw_input().lower()
		print 'yes' if 'problem' in line else 'no'
	except EOFError:
		break



