def mystery(lst):
    temp = lst[0]
    for i in range(1, len(lst)):
        lst[i-1] = lst[i]

    lst[-1] = temp

lst = [3,2,5,1,4]
mystery(lst)
print(lst)
