def get_lcm(a, b):
    multiple = a * b
    max_v = a
    if b > a:
        max_v = b

    for i in range(max_v, multiple):
        if i % a == 0 and i % b == 0:
            return i

    return multiple

print(get_lcm(6, 8))
print(get_lcm(12, 15))
