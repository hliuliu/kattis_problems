

n = int(raw_input())

pts  = [map(int, raw_input().split()) for _ in xrange(n)]

combs = '{{2018,0},{0,2018},{1118,1680},{1680,1118}, {-2018,0}, {0,-2018}, {-1118,1680}, {1118,-1680},{-1118,-1680},{1680,-1118},{-1680,1118},{-1680,-1118}}'.replace('{','(').replace('}',')')
combs = eval(combs)

ptss = set()

def nbrs(pt):
    x,y =pt
    for a,b in combs:
        yield (x+a,y+b)


count =0
for pt in pts:

    pt = tuple(pt)
    for pp in nbrs(pt):
        if pp in ptss:
            count+=1
        ptss.add(pt)
print count
