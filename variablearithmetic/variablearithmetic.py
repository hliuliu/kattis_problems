

vardefs={}

def convert(value):
	try:
		value = int(value)
		return value
	except:
		if value in vardefs:
			return vardefs[value]
		return value


expr = raw_input()

while expr!='0':
	if '=' in expr:
		x,y = expr.split(' = ')
		vardefs[x] = int(y)
	else:
		toks=expr.split(' + ')
		toks= map(convert,toks)
		toks.sort(key=type)
		num = 0
		while toks and type(toks[0])==int:
			num+=toks.pop(0)
		if num:
			toks.insert(0,str(num))
		print ' + '.join(toks)

	expr = raw_input()



