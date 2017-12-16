

n= int(raw_input())

class node(object):
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None
		self.maxval = n
		self.minval = 1

node_by_value=[None]*(n+1)

root = None

depth=[-1]*(n+1)

parent = [0]*(n+1)

order = [int(raw_input()) for _ in xrange(n)]

counter = 0

def insert(el):
	global counter,root
	if root==None:
		root = node(el)
		node_by_value[el]=root
		depth[el]=0
		for i in xrange(1,n+1):
			if i!=el:
				parent[i] = el
	else: 
		parent_node = node_by_value[parent[el]]
		node_by_value[el] = node(el)
		curr_node=node_by_value[el]
		if el> parent[el]:
			# insert right
			parent_node.right = curr_node
			curr_node.minval = parent[el]+1
			curr_node.maxval = parent_node.maxval
		else:
			parent_node.left = curr_node
			curr_node.minval = parent_node.minval
			curr_node.maxval = parent[el]-1
		depth[el] = depth[parent[el]]+1
		# print 'depth',depth[el]
		# print el,parent[el]
		for i in xrange(curr_node.minval,curr_node.maxval+1):
			if depth[i]<0:
				parent[i]=el
		counter+=depth[el]


	print counter








for el in order:
	insert(el)




