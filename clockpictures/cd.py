

n,m = map(int, raw_input().split())

while n or m:
    owns = set([int(raw_input()) for _ in xrange(n)])
    ct =0
    for _ in xrange(m):
        if int(raw_input()) in owns:
            ct += 1
    print ct
    n,m = map(int, raw_input().split())
