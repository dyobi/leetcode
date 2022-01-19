"448. Find All Numbers Disappeared in an Array"

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Input: nums = [4,3,2,7,8,2,3,1] / Output: [5,6]
# Input: nums = [1,1] / Output: [2]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        tmp = [i + 1 for i in range(len(nums))]

        return list(set(tmp) - set(nums))
