

l=map(int,raw_input().split())
l.sort()

d=dict(zip('ABC',l))

line = raw_input()

print ' '.join(map(str,[d[c] for c in line]))
