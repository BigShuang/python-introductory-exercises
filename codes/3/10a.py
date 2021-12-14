def mystery1(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


lst = [7, 4, 6, 9, 5, 2]
mystery1(lst)
print(lst)
