

line=raw_input()

d={}
while line:
	e,f=line.split()
	d[f]=e
	line=raw_input()

while 1:
	try:
		line=raw_input()
		print d.get(line,'eh')
	except EOFError:
		break





