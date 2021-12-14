def mystery2(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


lst = [7, 4, 6, 9, 5, 2]
mystery2(lst)
print(lst)
