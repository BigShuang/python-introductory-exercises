line = input()
a, b, c = line.split()
a = int(a)
b = int(b)
c = int(c)

if a > b:
    if c < b:
        print(b)  # a > b > c
    elif c < a:  # c >= b
        print(c)  # a > c >= b
    else:  # c >=b, a <= c
        print(a)  # c >= a > b
else: # a <= b
    if c < a:
        print(a)  # c < a <= b
    elif c < b:  # c >= a
        print(c)  # a <= c < b
    else:  # c >= b
        print(b)  # a <= b <= c
