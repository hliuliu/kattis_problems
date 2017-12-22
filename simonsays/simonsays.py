
n=int(raw_input())

say='Simon says'

for i in xrange(n):
	m=raw_input().strip()
	if m.startswith(say):
		m=m[len(say):]
		print m

