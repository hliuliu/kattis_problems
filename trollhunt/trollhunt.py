

b,k,g=map(int,raw_input().split())

n=k//g

print (b-1)//n+int(bool((b-1)%n))


