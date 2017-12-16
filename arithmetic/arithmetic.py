
bits=[]

octval  = raw_input()

hval = hex(int(octval,8))[2:].upper()

if hval[-1]=='L':
	hval=hval[:-1]

print hval

# for digit in octval:
# 	digit = int(digit)
# 	dbits = []
# 	for i in xrange(3):
# 		dbits.append(digit&1)
# 		digit>>=1
# 	dbits.reverse()
# 	bits.extend(dbits)

# offset = len(bits)%4

# for _ in xrange((4-offset)&3):
# 	bits.insert(0,0)

# def nexthex():
# 	h = 0
# 	for _ in xrange(4):
# 		h<<=1
# 		h+=bits.pop(0)
# 	return hex(h)[-1].upper()



# hexlist=[]

# while bits:
# 	hexlist.append(nexthex())

# print ''.join(hexlist)


