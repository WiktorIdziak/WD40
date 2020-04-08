import math

def proste(a1,b1,a2,b2):
    if(a1*a2==-1):
        print("Proste sa prostopadle")
    elif(a1==a2):
        print("Proste sa rownolwgle")
    else:
         print("Proste nie sa rownolwgle ani prostopadle")
print(proste(1,2,1,4))
print(proste(1,2,7,4))
print(proste(-1,2,1,4))