def sum_digits(num):
    s = 0
    while num > 0:
        last = num % 10
        s += last
        num = num // 10

    return s


print(sum_digits(999))
