
import sys

sys.setrecursionlimit(10000)



def full(cup,content,capacities):
	return content[cup]==capacities[cup]

def empty(cup,content,capacities):
	return content[cup]==0

def pour(cup1,cup2,content,capacities):
	diff1=content[cup1]
	diff2=capacities[cup2]-content[cup2]
	if diff1>diff2:
		content[cup1]-=diff2
		content[cup2]=capacities[cup2]
		return diff2
	else:
		content[cup1]=0
		content[cup2]+=diff1
		return diff1

'''
visited=set()
output={}
def minamount(level=0):
	global content
	print level
	if content[0]==v:
		return 0
	if tuple(content) in visited:
		if tuple(content) in output:
			return output[tuple(content)]
		return 'impossible'
	visited.add(tuple(content))
	ans='impossible'
	for c1 in xrange(n):
		for c2 in xrange(n):
			if c1!=c2 and not empty(c1,content,capacities) and not full(c2,content,capacities):
				x,y=content[c1],content[c2]
				#print content,c1,c2
				p=pour(c1,c2,content,capacities)
				res=minamount(level+1)
				if type(res)==int:
					ans=min(ans,p+res)
				#print 'after',ans
				content[c1],content[c2]=x,y
	output[tuple(content)]=ans
	return ans
'''

'''
def minamount(n,v,content,capacities):
	visited={tuple(content):0}
	q=[content]
	steps=set()
	while q:
		content=q.pop(0)
		level=visited[tuple(content)]
		if content[0]==v:
			steps.add(level)
			continue
		for c1 in xrange(n):
			for c2 in xrange(n):
				if c1!=c2 and not full(c2,content,capacities) and not empty(c1,content,capacities):
					next_content=list(content)
					p=pour(c1,c2,next_content,capacities)
					if tuple(next_content) not in visited:
						q.append((next_content))
						visited[tuple(next_content)]=level+p
					elif visited[tuple(next_content)]>level+p:
						visited[tuple(next_content)]=level+p
						q.append(next_content)
	if steps:
		return min(steps)
	return 'impossible'
'''

def getlevel(content,parent):
	s=0
	while content!=None:
		val,content=parent[tuple(content)]
		s+=val
	return s

'''# wrong?
def getlevel(content,parent):
	if content==None:
		return 0
	val,next_content=parent[tuple(content)]
	parent[tuple(content)]=(val+getlevel(next_content,parent),None)
	return parent[tuple(content)][0]
'''



def minamount(n,v,content,capacities):
	visited={tuple(content)}
	parent={tuple(content):(0,None)}
	q=[content]
	steps=[]
	while q:
		content=q.pop(0)
		#level=visited[tuple(content)]
		if content[0]==v:
			steps.append(content)
			continue
		for c1 in xrange(n):
			for c2 in xrange(n):
				if c1!=c2 and not full(c2,content,capacities) and not empty(c1,content,capacities):
					next_content=list(content)
					p=pour(c1,c2,next_content,capacities)
					if tuple(next_content) not in visited:
						q.append((next_content))
						#visited[tuple(next_content)]=level+p
						visited.add(tuple(next_content))
						parent[tuple(next_content)]=(p,content)
					elif getlevel(next_content,parent)>getlevel(content,parent)+p:
						#visited[tuple(next_content)]=level+p
						#q.append(next_content)
						parent[tuple(next_content)]=(p,content)
	if steps:
		return min(map(lambda con: getlevel(con,parent) , steps))
	return 'impossible'






capacities=map(int,raw_input().split())

n=capacities.pop(0)

v=capacities.pop()

content=[0]*n

content[0]=capacities[0]

print minamount(n,v,content,capacities)

