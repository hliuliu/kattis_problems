


x,y,z=map(int,raw_input().split())
exp='%d%s%d'
for op in '+-*/':
	expsub=exp%(x,op,y)
	if eval(expsub)==z:
		print expsub+'='+str(z)
		break
	expsub=exp%(y,op,z)
	if eval(expsub)==x:
		print str(x)+'='+expsub
		break



