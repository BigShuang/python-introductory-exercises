def print_histogram(lst):
    max_h = lst[0]
    for item in lst:
        if item > max_h:
            max_h = item

    for ri in range(max_h, 0, -1):
        for item in lst:
            if item >= ri:
                print("#", end="")
            else:
                print(" ", end="")

        print()


lst = [1, 3, 2, 0, 5, 4, 1, 4]
print_histogram(lst)
