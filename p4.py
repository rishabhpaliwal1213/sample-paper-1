import math
a=list(map(int,input().split()))
c=50
h=30
for i in a:
   print(int(math.sqrt((2*c*i/h))),end=',')
