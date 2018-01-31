



def largest_deg(line):
	n = len(line)
	matrix= [[n]*(n-deg+1) for deg in xrange(n)]
	for deg in xrange(n):
		if deg==0:
			for i in xrange(n+1):
				matrix[0][i]=i+1
		else:
			row=matrix[deg-1]
			for i,begin in enumerate(row):
				while begin<len(row)-1:
					if line[begin+deg-1]==line[i+deg-1]:
						matrix[deg][i]=begin
						break
					begin=row[begin]
			row = matrix[deg]
			visited = [False]*len(row)
			for i,begin in enumerate(row):
				if begin<len(row):
					visited[begin]=True
					visited[i] = True
			if not all(visited):
				return deg-1

	return n-1









while 1:
	try:
		line = raw_input()
	except EOFError:
		break
	else:
		print largest_deg(line)





