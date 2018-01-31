
import re
t=int(raw_input())


def gcd(a,b):
    b,a=sorted([a,b])
    while b:
        r=a%b
        a,b=b,r
    return a


def findn(p,q):
    if p==q:
        return 1
    if p<q:
        return 2*findn(p,q-p)
    return 2*findn(p-q,q)+1



for _ in xrange(t):
    k,p,q=map(int,re.split('/|\s+',raw_input()))
    d=gcd(p,q)
    p/=d
    q/=d
    print k,findn(p,q)
    
