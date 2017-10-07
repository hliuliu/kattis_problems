
def getpts(a,b,c):
    if a!=0:
        return -c/float(a),0
    return 0, -c/float(b)


def calc(x,y):
    ans=0
    for (p,q),(x0,y0) in zip(dirs,ppts):
        x0,y0 = proj(q,-p,x0-x,y0-y)
        x0+=x
        y0+=y
        d = det([[p,q],[x0-x,y0-y]])
        if d>0:
            ans+=1
        ans = ans<<1
    return ans


def proj(x0,y0,x1,y1):
    mult = dot(x0,y0,x1,y1)/float(x0**2+y0**2)
    return x0*mult,y0*mult

def dot(x0,y0,x1,y1):
    return x0*x1+y0*y1

def det(A):
    [a,b],[c,d] = A
    return a*d-b*c

def intersect(p1,v1,p2,v2):
    p1x,p1y = p1
    v1x,v1y = v1
    p2x,p2y = p2
    v2x,v2y = v2
    M= [[v2x,-v1x], [v2y, -v1y]]
    p = [p1x-p2x, p1y-p2y]
    if det(M)!=0:
        s,t = matmult(matinv(M), p)
        return p1x+t*v1x, p1y+t*v1y
    return None

def matinv(A):
    [a,b],[c,d] = A
    dem = float(det(A))
    return [[d/dem, -b/dem],[-c/dem, a/dem]]

def matmult(A,v):
    [a,b],[c,d] = A
    return [a*v[0]+b*v[1], c*v[0]+d*v[1]]

n,m,r = map(int, raw_input().split())
candles = [map(int, raw_input().split()) for _ in xrange(n)]

dirs,ppts = [],[]


def incircle(x,y,r):
    return x**2+y**2<r**2


def countpcs(i,r):
    intn = set()
    for j in xrange(i):
        p = intersect(ppts[j],dirs[j],ppts[i], dirs[i])
        # print p
        if p is not None:
            p = map(lambda t: round(t,6),p)
            x,y =p
            if incircle(x,y,r):
                intn.add((x,y))
    # print intn
    return len(intn)+1




pcs = 1

for i in xrange(m):
    a,b,c = map(int,raw_input().split())
    dirs.append((b,-a))
    ppts.append(getpts(a,b,c))
    # print dirs, ppts
    pcs += countpcs(i,r)
    # print pcs

locs = set()
for x, y in candles:
    val = calc(x,y)
    if val in locs:
        print 'no'
        break
    locs.add(val)
else:
    print 'yes' if len(locs)==pcs else 'no'
