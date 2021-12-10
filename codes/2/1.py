def check_five(lst, c):
    count = 0
    for item in lst:
        if item == c:
            count += 1

            if count >= 5:
                return True
        else:
            count = 0

    return False


lst = ['X', 'O', ' ', 'X', 'X', 'X', ' ', 'X', ' ', 'O', ' ', 'O', 'X']
c = "X"
print(check_five(lst, c))
