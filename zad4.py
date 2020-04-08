import math

def mon (a,b):
    if(a>0):
        print("Funkcja y="+str(a)+"x+"+str(b)+" jest rosnąca")
        return a
    elif(a<0):
        print("Funkcja y="+str(a)+"x+"+str(b)+" jest malejaca")
        return a
    else:
        print("Funkcja y="+str(a)+"x+"+str(b)+" jest stała")
        return a
print(mon(1,4))
print(mon(-13,5))
print(mon(0,43))