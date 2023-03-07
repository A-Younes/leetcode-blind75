nums = [1,2,3,4]

def compare_keys(key_list):
    store_keys = {}
    for i in key_list:
        if i in store_keys:
            return True
        store_keys[i] = "None"
        # print(store_keys)
    return False

print(compare_keys(nums))