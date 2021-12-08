s = input()
m, n = s.split(" ")
m = int(m)
n = int(n)

for ri in range(m):
    for ci in range(n):
        v = ( ri + 1 ) * ( ci + 1 )
        print(v, end=" ")
    print()

