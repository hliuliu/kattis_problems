
import sys

seen=[False]*42

for val in sys.stdin:
	n=int(val)
	seen[n%42]=True

print seen.count(True)


