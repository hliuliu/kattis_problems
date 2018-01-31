

raw_input()

sentence = raw_input().split()

sts = set(sentence)

m = int(raw_input())

wdict = {}

while m:
    m-=1
    du,eng,status = raw_input().split()
    if du in sts:
        if du not in wdict:
            wdict[du] = {}
        wdict[du][eng] = 'in' not in status

def gettr(key):
    for tr in wdict[key]:
        return tr

def prod(seq):
    ans = 1
    for a in seq:
        ans *=a
    return ans

def makecounts():
    right , total = [],[]
    for key in sentence:
        right.append(0)
        total.append(0)
        for tr in wdict[key]:
            total[-1]+=1
            if wdict[key][tr]:
                right[-1]+=1
    right, total = map(prod, [right,total])
    print right, 'correct'
    print total-right, 'incorrect'

if all([len(v)==1 for k,v in wdict.iteritems()]):
    trans = map(gettr,sentence)
    print ' '.join(trans)
    correct = all([all(wdict[key].values()) for key in wdict])
    print 'correct' if correct else 'incorrect'
else:
    makecounts()







