
from datetime import datetime as dt

print dt.strptime('%02d %02d, 2009'%(tuple(map(int,raw_input().split()))),'%d %m, %Y').strftime('%A')

