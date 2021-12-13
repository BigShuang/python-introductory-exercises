def get_two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j

    return -1, -1


nums = [3,3]
target = 6
print(get_two_sum(nums, target))
