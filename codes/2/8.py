def jump_print(lst):
    record = []
    current = 0

    while current not in record:
        record.append(current)
        print(lst[current])
        current += lst[current]
        current = current % len(lst)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jump_print(lst)
