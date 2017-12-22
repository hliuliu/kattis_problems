



class trie(object):
	def __init__(self,depth):
		self.wordcount=0
		if depth:
			self.children=[trie(depth-1) for _ in xrange(26)]
	def insert(word):
		self.wordcount+=1
		if word:
			self.children[ord(word.pop(0))-ord('a')].insert(word)
	def find(prefix):
		if not prefix:
			return self.wordcount
		return self.children[ord(prefix.pop(0))-ord('a')].find(prefix)




t={}

n=int(raw_input())

for _ in xrange(n):
	line=raw_input()
	print t.get(line,0)
	pref=''
	for c in line:
		t[pref]=t.get(pref,0)+1
		pref+=c
	t[line]=t.get(line,0)+1


