

allow=map(str,range(10))
let='a'
for i in range(10,36):
	allow.append(let)
	let=chr(ord(let)+1)
basedict={j:i for i,j in enumerate(allow)}

#print basedict

def convert(val,base):
	if base==1:
		if val!='1'*len(val):
			return None
		return len(val)
	x=0
	for i in val:
		x*=base
		d=basedict.get(i,37)
		if not 0<=d<base:
			return None
		x+=d
	if x>2**32-1:
		return None
	return x

#print convert('1000',2)


def safeeval(exp):
	try:
		return eval(exp)
	except:
		return None

n= int(raw_input())

for i in xrange(n):
	exp=raw_input()
	toks=exp.split()
	a,op,b,_,c=toks
	valid=[]
	for base in xrange(1,37):
		ab=convert(a,base)
		if ab==None:
			continue
		bb=convert(b,base)
		if bb==None:
			continue
		cb=convert(c,base)
		if cb==None:
			continue
		res=safeeval(str(ab)+op+str(bb))
		if res!=None and res==cb:
			if op=='/':
				if cb*bb==ab:
					valid.append(base)
			else:
				valid.append(base)
	#print valid
	if valid:
		print ''.join(map(lambda x: '0' if x==36 else allow[x],valid))
	else:
		print 'invalid'




