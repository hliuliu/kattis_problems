







def array(*shape):
	if not shape:
		return 0
	r,shape=shape[0],shape[1:]
	return [array(*shape) for _ in xrange(r)]


table=array(29,29,15)

table[14][14][0]=1

for step in xrange(1,15):
	for i in xrange(28):
		for j in xrange(28):
			if i>0:
				table[i][j][step]+=table[i-1][j][step-1]
			if j>0:
				table[i][j][step]+=table[i][j-1][step-1]
			if i>0 and j>0:
				table[i][j][step]+=table[i-1][j-1][step-1]
			if i<29:
				table[i][j][step]+=table[i+1][j][step-1]
			if j<29:
				table[i][j][step]+=table[i][j+1][step-1]
			if i<29 and j<29:
				table[i][j][step]+=table[i+1][j+1][step-1]





# def f(n,k,a=0):
# 	if table[n][k][a]>=0:
# 		return table[n][k][a]
# 	if n in [0,1]:
# 		table[n][k][a]=1 if n==k else 0
# 		return table[n][k][a]
# 	if k==0:
# 		table[n][k][a]=6*f(n-1,1)
# 		return table[n][k][a]
# 	if k==1:
# 		table[n][k][a]=f(n-1,0)+2*f(n-1,1)+f(n-1,2,0)+2*f(n-1,2,1)
# 		return table[n][k][a]
# 	if a==0:
# 		table[n][k][a]=f(n-1,k-1,0)+2*f(n-1,k,1)+2*f(n-1,k+1,1)+f(n-1,k+1,0)
# 		return table[n][k][a]
# 	table[n][k][a]=f(n-1,k-1,0)+2*f(n-1,k,0)+f(n-1,k-1,1)+2*f(n-1,k+1,1)
# 	return table[n][k][a]




t=int(raw_input())

for _ in xrange(t):
	n=int(raw_input())
	print table[14][14][n]



