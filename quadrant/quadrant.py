

def quad(x,y):
	if x>0:
		return 1 if y>0 else 4
	return 2 if y>0 else 3

x = int(raw_input())
y = int(raw_input())

print quad(x,y)


