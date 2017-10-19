
# Accepted :)

def transform(r,gem):
	x,y= gem
	return x*r+y, y-x*r


def binsearch(key,tail,arr,start,end):
	while end-start>2:
		mid = (start+end)/2
		if arr[tail[mid]]>key:
			end = mid+1
		else:
			start=mid+1

	return start if arr[tail[start]]>key else start+1


def LIS(arr):
	n = len(arr)
	tail = [0]*n
	sz=1
	for i in xrange(1,n):
		if arr[i]<arr[tail[0]]:
			tail[0]=i
		elif arr[i]>=arr[tail[sz-1]]:
			tail[sz] = i
			sz+=1
		else:
			j = binsearch(arr[i],tail,arr,1,sz)
			tail[j]=i
	return sz



n,r,w,h = map(int, raw_input().split())

gems = [transform(r,map(int,raw_input().split())) for _ in xrange(n)]

gems.sort()

print LIS(map(lambda x: x[1], gems))


