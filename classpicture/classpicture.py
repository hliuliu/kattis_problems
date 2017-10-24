



def dfs(path,students,n,used,start,dislike):
	path.append(students[start])
	if len(path)==n:
		return True
	used[start] = True
	for i in xrange(n):
		if not used[i] and students[i] not in dislike[path[-1]]:
			if dfs(path,students,n,used,i,dislike):
				return True
	path.pop()
	used[start]=False
	return False





while 1:
	try :
		n = int(raw_input())
	except EOFError:
		break
	else:
		students = [raw_input() for _ in xrange(n)]
		students.sort()
		lookup = {j:i for i,j in enumerate(students)}
		dislike = {s:set() for s in students}
		m= int(raw_input())
		for _ in xrange(m):
			s1,s2 = raw_input().split()
			dislike[s1].add(s2)
			dislike[s2].add(s1)

		path = []
		used =[False]*n
		for i in xrange(n):
			if dfs(path,students,n,used,i,dislike):
				print ' '.join(path)
				break
		else:
			print 'You all need therapy.'
		





