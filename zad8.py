import math


def suma(a1=1, r=1, ile=10):
    if ile == 0:
        return 0.0
    elif ile == 1:
        s = a1
    else:
        for i in range(ile):
            a1 += r
            s = a1

    print(s)


print(suma(24, -5, 10))

