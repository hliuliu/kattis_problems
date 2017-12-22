
import re


line=raw_input()


stack=[]

for c in line:
	if c=='<':
		stack.pop()
	else:
		stack.append(c)

line=''.join(stack)


print line






