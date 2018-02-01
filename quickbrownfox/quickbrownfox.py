
import string

lettersa=string.ascii_lowercase


n=int(raw_input())

for j in xrange(n):
	letters=set(lettersa)
	m=raw_input().strip().lower()
	l=[]
	for i in m:
		letters.discard(i)

	if not letters:
		print 'pangram'
	else:
		print 'missing', ''.join(sorted(letters))


