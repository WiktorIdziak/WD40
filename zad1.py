print("1/x x należy <1,10>")
A = [1/x for x in range(1, 11)]
print(A)
print("1,2,4,8,...,2**10")
B = [2**x for x in range(11)]
print(B)
print("x należy do B i x jest podzielne przez 4")
C = [x for x in B if x % 4 == 0]
print(C)
