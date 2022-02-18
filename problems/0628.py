"628. Maximum Product of Three Numbers"

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

# Input: nums = [1,2,3] / Output: 6
# Input: nums = [1,2,3,4] / Output: 24
# Input: nums = [-1,-2,-3] / Output: -6

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        t = sorted(nums)[::-1]
        return max(t[0] * t[1] * t[2], t[0] * t[-1] * t[-2])
