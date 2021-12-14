def get_min(*args):
    # 其实也可以直接使用python内置函数`min`
    # 我这里相当手动实现了一遍
    min_v = args[0]
    for v in args:
        if v < min_v:
            min_v = v

    return min_v

def generate_matrix(m, n):
    matrix = [
        [get_min(ri, ci, n-ci-1, m-ri-1) for ci in range(n)]
        for ri in range(m)
    ]

    return matrix


board = generate_matrix(7, 10)
for row in board:
    print(row)
