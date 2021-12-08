# https://leetcode.com/problems/spiral-matrix/

direction = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]


def get_spiral_matrix(m, n):
    matrix = [
        [0 for ci in range(n)] for ri in range(m)
    ]

    ci, ri = -1, 0
    di = 0
    count = 0

    while count < m * n:
        dc, dr = direction[di]
        nc, nr = ci + dc, ri + dr
        if 0 <= nc < n and 0 <= nr < m:
            if matrix[nr][nc] == 0:
                count += 1
                matrix[nr][nc] = count
                ci, ri = nc, nr
                continue

        di += 1
        di %= 4

    return matrix



board = get_spiral_matrix(5, 4)
for row in board:
    print(row)
