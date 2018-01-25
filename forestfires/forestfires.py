

def rnext(r):
    return (r*5171+13297)%50021

def nbhr(x):
    if x>=100:
        yield x-100
    if x<10000-100:
        yield x+100
    if x%100:
        yield x-1
    if x%100<99:
        yield x+1

def query(A,B, trees):
    if A==B:
        return True
    q = [A]
    vis = 0
    vis = vis ^ (1<<A)
    while q:
        A = q.pop(0)
        for C in nbhr(A):
            if trees&(1<<C) and not vis&(1<<C):
                if C==B:
                    return True
                q.append(C)
                vis = vis ^ (1<<C)
    return False




def simulate(r,n):
    trees = 0
    L = []
    ct =0

    for i in xrange(n):
        m = r%10000
        while trees&(1<<m):
            r = rnext(r)
            m = r%10000

        L.append(m)
        trees |= (1<<m)

        a = r%(i+1)
        b = r%(i+1)

        A = L[a]
        B = L[b]

        if query(A,B,trees):
            ct += 1

        if i%100 == 99:
            print ct
            ct = 0






while 1:
    try:
        r,n = map(int,raw_input().split())
    except EOFError:
        break
    else:
        simulate(r,n)
