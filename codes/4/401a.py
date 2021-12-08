# https://leetcode.com/problems/spiral-matrix/

def get_spiral_matrix(m, n):
    matrix = [
        [0 for ci in range(n)] for ri in range(m)
    ]
    min_v = m
    if n < m:
        min_v = n

    layer = (min_v + 1) // 2
    count = 0
    for li in range(layer):
        for ci in range(li, n-li):
            count += 1
            matrix[li][ci] = count

        for ri in range(li + 1, m-li-1):
            count += 1
            matrix[ri][n-li-1] = count

        if li < m-li-1:
            for ci in range(n-li-1, li-1, -1):
                count += 1
                matrix[m-li-1][ci] = count

        if li < n-li-1:
            for ri in range(m-li-2, li, -1):
                count += 1
                matrix[ri][li] = count

    return matrix


board = get_spiral_matrix(6, 5)
print(board)
