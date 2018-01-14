

n= int(raw_input())

items={}

while n:
    items={}
    for i in xrange(n):
        entry=raw_input().split()
        cust,itemlist=entry[0],entry[1:]
        for item in itemlist:
            items[item]=items.get(item,[])
            items[item].append(cust)
    for it in sorted(items):
    	items[it].sort()
        print it, ' '.join((items[it]))
    print 
    n=int(raw_input())

