
import string

ct=dict(zip(string.ascii_lowercase,[0]*26))

word=raw_input()

for c in word:
	ct[c]+=1

numodd=0

for c in ct:
	numodd+=ct[c]&1

print max(0,numodd-1)



