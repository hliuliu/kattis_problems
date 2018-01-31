
from math import atan,sqrt,pi

def get_velocity(a,b,s,m,n):
    dx=m*a
    dy=n*b
    vx=float(dx)/s
    vy=float(dy)/s
    return vx,vy
    
#print raw_input().replace(' ','#')

#exit()

a,b,s,m,n=map(int,raw_input().split())
#print a,b,s,m,n

while s:
    vx,vy=get_velocity(a,b,s,m,n)
    if not vx:
        angle=90.0
    else:
        angle=atan(vy/vx)/pi*180
    v=sqrt(vx**2+vy**2)
    print '%.2f %.2f'%(angle,v)
    a,b,s,m,n=map(int,raw_input().split())





