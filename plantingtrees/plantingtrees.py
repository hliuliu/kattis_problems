

n= int(raw_input())

trees=map(int,raw_input().split())
trees.sort(reverse=True)

print max((i+j for i,j in enumerate(trees,2)))



