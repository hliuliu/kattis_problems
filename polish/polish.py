
def to_value(x):
	try: 
		return int(x)
	except:
		return x


class node(object):
	def __init__(self, value, left=None,right=None):
		self.value= value
		self.left = left
		self.right = right


def build_tree(tokens):
	if not tokens:
		return None
	root = node(tokens.pop(0))
	if root.value not in list('+-*'):
		return root
	root.left = build_tree(tokens)
	root.right = build_tree(tokens)
	return root


def reduce_tree(root):
	if root is None:
		return None
	root.left = reduce_tree(root.left)
	root.right = reduce_tree(root.right)
	if root.value in list('+-*'):
		if type(root.left.value) is int and type(root.right.value) is int:
			return node(eval(
				'(%d)%s(%d)'%(root.left.value,root.value,root.right.value)
				))
	return root

def preorder(root):
	if root is not None:
		yield str(root.value)
		for v in preorder(root.left):
			yield v
		for v in preorder(root.right):
			yield v

num =1
while True:
	try:
		tokens = map(to_value, raw_input().split())
		root = build_tree(tokens)
		root = reduce_tree(root)
		print 'Case %d:'%num, ' '.join(preorder(root))
		num+=1
	except EOFError:
		break



