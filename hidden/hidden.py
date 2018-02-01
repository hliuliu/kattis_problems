

pwd, msg = raw_input().split()

pwd = list(pwd)

for c in msg:
	if not pwd:
		print 'PASS'
		break
	if c in pwd:
		if c != pwd[0]:
			print 'FAIL'
			break
		pwd.pop(0)
else:
	print 'PASS' if not pwd else 'FAIL'



