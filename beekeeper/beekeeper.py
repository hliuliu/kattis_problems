


def count_dv(word):
	count=0
	for i in xrange(len(word)-1):
		if word[i]==word[i+1] and word[i] in 'aeiouy':
			count+=1
	return count


n=int(raw_input())

while n:
	print max([raw_input().strip() for _ in xrange(n)],key=count_dv)
	n=int(raw_input())



