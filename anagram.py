def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    new_dict = {}
    other_dict = {}
    for i in range(len(s)):
        new_dict[s[i]] = 1 + new_dict.get(s[i], 0)
        other_dict[t[i]] = 1 + other_dict.get(t[i], 0)

        # print(new_dict)
        # print(other_dict)

    for c in new_dict:
        if new_dict[c] != other_dict.get(c, 0):
            return False
    return True

str1 = "hello"
str2 = "ellho"
isAnagram(str1, str2)
