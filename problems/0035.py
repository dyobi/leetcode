"35. Search Insert Position"

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# Input: nums = [1,3,5,6], target = 5 / Output: 2

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if (target not in nums) :
            nums = sorted(nums + [target])
        
        return nums.index(target)