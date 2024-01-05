def first_non_repeating_char(string):
    string_dict = {}
    for letter in string:
        string_dict[letter] = string_dict.get(letter, 0) + 1
    for letter, value in string_dict.items():
        if value == 1: return letter
    return None
        



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )

def group_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        sorted_str = "".join(sorted(string))
        if sorted_str not in anagram_dict:
            anagram_dict[sorted_str] = [string]
        else:
            anagram_dict[sorted_str].append(string)
    return list(anagram_dict.values())




print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )

def two_sum(nums, target):
    nums_dict = {}
    for idx, num in enumerate(nums):
        if (target - num) in nums_dict:
            return[nums_dict[(target - num)], idx]
        nums_dict[num] = idx
    return []
    # return nums_dict
      
print(two_sum([5, 1, 7, 2, 9, 3], 10))  


def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
    return []


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )