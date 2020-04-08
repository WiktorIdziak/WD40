import math

def kolo (a,b,x=0,y=0):
    r=((x-a)**2)+(y-b)**2
    wyn=math.sqrt(r)
    print(wyn)
print(kolo(4,3))
print(kolo(2,2,6,5))
