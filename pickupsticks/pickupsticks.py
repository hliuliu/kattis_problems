
# Accepted :)
n,m = map(int,raw_input().split())

G = {}

for _ in xrange(m):
    a, b= map(int, raw_input().split())
    G[a] = G.get(a,set())
    G[a].add(b)


indeg = [0]*(n+1)

for a in G:
    for b in G[a]:
        indeg[b]+=1

q, l =[a for a in xrange(1,n) if not indeg[a]],[]


while q:
    u = q.pop(0)
    l.append(u)
    for v in G.get(u,set()):
        indeg[v]-=1
        if not indeg[v]:
            q.append(v)

print 'IMPOSSIBLE' if len(l)<n else '\n'.join(map(str,l))
