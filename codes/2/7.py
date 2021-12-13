def clear_duplication(lst):
    clear_indexes = []
    record = []
    for index in range(len(lst)):
        item = lst[index]
        if item in record:
            clear_indexes.append(index)
        else:
            record.append(item)

    for index in clear_indexes[::-1]:  # 注意，要从后往前删除
        lst.pop(index)


lst = [8, 3, 2, 5, 1, 1, 3, 6, 1, 9, 2, 1]
clear_duplication(lst)
print(lst)
