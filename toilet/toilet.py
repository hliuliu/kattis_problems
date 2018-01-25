



seq=raw_input()


su,sd,sl=seq[0]*3

seq=seq[1:]

nu,nd,nl=0,0,0

for s in seq:
	nu+=int(bool(s!=su))
	nd+=int(bool(s!=sd))
	nl+=int(bool(s!=sl))
	su,sd,sl=s,s,s
	nu+=int(bool(s!='U'))
	nd+=int(bool(s!='D'))
	su,sd='UD'

print nu
print nd
print nl



