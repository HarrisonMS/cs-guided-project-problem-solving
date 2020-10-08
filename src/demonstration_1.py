"""
Given a list of integers and a target value, return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums[i+1:])+1):
            if nums[i] + nums[j] == target:
                return i, j
print(two_sum([8,12,17,7], 15))
#(0, 3)

def two_sum(nums, target):
    for index1, num1 in enumerate(nums):
        for index2, num2 in enumerate(nums):
            if index1 is not index2 and num1 + num2 == target:
                return [index1, index2]

def two_sum(nums, target):
    for index1, x in enumerate(nums):
        diff = target - x
        index2 = 0
        if diff in nums:
            index2 = nums.index(diff)
            return [index1, index2]
        else:
            continue
def two_sum(nums, target):

    def Convert(lst):
        res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
        print(res_dct)

    print(Convert(nums))

two_sum([3, 8, 12, 17], 15)