

raw_input()

nums=map(int, raw_input().split())

member={}
for i,n in enumerate(nums):
    if n in member:
        member[n]=None
    else:
        member[n]=i

unique=[n for n in member if member[n]!=None]

if not unique:
    print ('none')
else:
    print (member[max(unique)]+1)
