

m = int(raw_input())


wordcount = {}
users = {}


for _ in xrange(m):
	tokens = raw_input().split()
	user = tokens.pop(0)
	if user not in users:
		users[user] = set()
	for t in tokens:
		 users[user].add(t)
		 wordcount[t] = wordcount.get(t,0)+1

allused = set(wordcount)

for user in users:
	allused &= users[user]

allused = list(allused)
allused.sort(key = lambda x: (-wordcount[x], x))

if not allused:
	print 'ALL CLEAR'
else:
	print '\n'.join(allused)


