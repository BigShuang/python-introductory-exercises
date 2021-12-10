def cal_rc(m, n, order):
    ri = order // n
    ci = order % n
    return ri, ci


print(cal_rc(3, 4, 9))
print(cal_rc(6, 5, 18))
