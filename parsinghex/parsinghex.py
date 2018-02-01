
import re


while 1:
	try:
		line=raw_input()
		#prefs=re.findall('(0x)',line,re.I)
		occs=re.split('(0x)',line,flags=re.I)[1:]
		#print occs
		nums=[]
		while occs:
			nums.append(occs.pop(0)+re.search('^([0-9a-f])*',occs.pop(0),re.I).group(0)[:8])
		for n in nums:
			print n,int(n,16)
		#print occs
	except EOFError:
		break








