


def next_perm(perm, ctr):
	if ctr==0:
		return False # no next perm, only 1 perm on 1 element
	index = perm.index(ctr)
	if dirs[ctr]==0:
		if index>0:
			perm[index],perm[index-1]=perm[index-1],perm[index]
			return True
		dirs[ctr]= 1
		del perm[0]
		if not next_perm(perm,ctr-1):
			perm.insert(0,ctr)
			return False
		perm.insert(0,ctr)
		return True
	if index<ctr:
		perm[index],perm[index+1]=perm[index+1],perm[index]
		return True
	dirs[ctr]=0
	del perm[-1]
	if not next_perm(perm,ctr-1):
		perm.append(ctr)
		return False
	perm.append(ctr)
	return True








def print_perm(perm):
	perm = map(lambda l: l+1,perm)
	print ' '.join(map(str,perm))


def plain_changes(n):
	perm = range(n)
	print_perm(perm)
	while next_perm(perm,n-1):
		print_perm(perm)


n= int(raw_input())

dirs= [0]*n # 0 for left


plain_changes(n)

