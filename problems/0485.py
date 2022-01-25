"485. Max Consecutive Ones"

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Input: nums = [1,1,0,1,1,1] / Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Input: nums = [1,0,1,1,0,1] / Output: 2

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        s = "".join([str(i) for i in nums]).split("0")
        return len(max(s))
