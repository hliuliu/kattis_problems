

drm = raw_input()

lton = lambda x: ord(x)-ord('A')

ntol = lambda x: chr(x+ord('A')) 

def shift(letter,offset):
	return ntol((lton(letter)+offset)%26)


n = len(drm)
m1,m2= drm[:n/2], drm[n/2:]

r1 = sum(map(lton, m1))
r2 = sum(map(lton, m2))

m1 = [shift(x,r1) for x in m1]
m2 = [shift(x,r2) for x in m2]

m =''
for x,y in zip(m1,m2):
	m+=shift(x,lton(y))

print m

