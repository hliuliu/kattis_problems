

pcs=[1,1,2,2,2,8]

found=map(int,raw_input().strip().split())

print ' '.join([str(i-j) for i,j in zip(pcs,found)])

