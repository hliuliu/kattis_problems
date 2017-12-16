


def process(command):
	global wtonum,numtow
	ctype=command.pop(0)
	if ctype=='clear':
		wtonum={}
		numtow={}
	elif ctype=='def':
		word,num=command
		if word in wtonum:
			del numtow[wtonum[word]]
		wtonum[word]=int(num)
		numtow[int(num)]=word
	else:
		word=command.pop(0)
		if word not in wtonum:
			return 'unknown'
		num=wtonum[word]
		while command!=['=']:
			op,word=[command.pop(0) for _ in [1,2]]
			if word not in wtonum:
				return 'unknown'
			if op=='+':
				num+=wtonum[word]
			else:
				num-=wtonum[word]
		if num not in numtow:
			return 'unknown'
		return numtow[num]





wtonum={}
numtow={}

while 1:
	try:
		cstr=raw_input()
		command=cstr.split()
		cstr=' '.join(command[1:])
		res=process(command)
		if res!=None:
			print cstr,res
	except EOFError:
		break

