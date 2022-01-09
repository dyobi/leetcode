"283. Move Zeroes"

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Input: nums = [0,1,0,3,12] / Output: [1,3,12,0,0]
# Input: nums = [0] / Output: [0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [i for i in nums if i != 0] + [i for i in nums if i == 0]