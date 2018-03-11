

#TLE:(

n = int(raw_input())

A = [int(raw_input()) for _ in xrange(n)]

# S = sorted(A)

# revl = {j:i for i,j in enumerate(S)}

# perm = map(lambda x: revl[x],A)



# count = 0

# for i,j in enumerate(perm):
# 	if i<j:
# 		count += j-i

# print count

nswaps = 0

def mysort(A,start,end):
	if end-start<2:
		return
	global nswaps
	mid = start+end
	mid >>= 1
	mysort(A,start,mid)
	mysort(A,mid,end)
	left,right = mid-1, end-1
	while left>=start and right>left:
		while right>left and A[right]>A[left]:
			right -= 1
		A[left:right+1] = A[left+1:right+1]+[A[left]]
		nswaps += right-left
		right -= 1
		left -= 1


mysort(A,0,n)
print nswaps


