

def overlap(p):
    m = len(p)
    ol = [-1]+[0]*m
    for i in xrange(m):
        ol[i+1] = ol[i]+1
        while ol[i+1]>0 and p[i]!=p[ol[i+1]]:
            ol[i+1]= ol[ol[i+1]-1] + 1

    return ol



def kmp(p,t):
    m = len(p)
    n = len(t)
    j=0
    ol = overlap(p)
    for i in xrange(n):
        while 1:
            if t[i]==p[j]:
                j+=1
                if j==m:
                    return True
                break
            elif j==0:
                break
            else:
                j = ol[j]
    return False


n= int(raw_input())

fst = map(int, raw_input().split())
snd = map(int, raw_input().split())

fst.sort()
snd.sort()

fstd = []
sndd = []

for i in xrange(n-1):
    fstd.append(fst[i+1]-fst[i])
    sndd.append(snd[i+1]-snd[i])

fstd.append(360000-sum(fstd))
sndd.append(360000-sum(sndd))


print 'possible' if kmp(sndd,fstd*2) else 'impossible'
