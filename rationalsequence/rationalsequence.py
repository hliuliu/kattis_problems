
import re,sys

t=int(raw_input())

sys.setrecursionlimit(10000)



def gcd(a,b):
    b,a=sorted([a,b])
    while b:
        r=a%b
        a,b=b,r
    return a


def findn(p,q):
    # if p==q:
    #     return 1
    # if p<q:
    #     return 2*findn(p,q-p)
    # return 2*findn(p-q,q)+1
    track=[]
    while p!=q:
        if p<q:
            track.append(0)
            p,q=p,q-p
        else:
            track.append(1)
            p,q=p-q,q
    ans=1
    while track:
        ans=2*ans+track.pop()
    return ans

def getfrac(n):
    if n==1:
        return 1,1
    p,q=getfrac(n>>1)
    if not n&1:
        return p,p+q
    return p+q,q


def nxt(p,q):
    if p<q:
        return q,q-p
    p,q=nxt(p-q,q)
    return p,p+q


for _ in xrange(t):
    k,p,q=map(int,re.split('/|\s+',raw_input()))
    #n=findn(p,q)
    pn,qn=nxt(p,q)
    print k,'%d/%d'%(pn,qn)
    
