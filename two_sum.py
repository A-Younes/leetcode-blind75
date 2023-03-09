def two_sum(nums_list, target_num):
    i = 0
    j = 1

    while nums_list:
        if nums_list[i] + nums_list[j] == target_num:
            return i, j
        j += 1
        
        if j >= len(nums_list):
            i += 1
            j = i + 1

nums = [1,3,5,7,9]
target = 14

print(two_sum(nums, target))
