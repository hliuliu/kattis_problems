


n = int(raw_input())


def is_arith(seq):
	d= None
	for i in xrange(len(seq)-1):
		if d is None:
			d = seq[i+1]-seq[i]
		else:
			if seq[i+1]-seq[i]!=d:
				return False
	return True




for _ in xrange(n):
	seq = map(int, raw_input().split()[1:])
	oseq = sorted(seq)
	if is_arith(seq):
		print 'arithmetic'
	elif not is_arith(oseq):
		print 'non-arithmetic'
	else:
		print 'permuted arithmetic'



