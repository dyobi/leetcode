"27. Remove Element"

# Input: nums = [0,1,2,2,3,0,4,2], val = 2 / Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        while (val in nums) :
            nums.remove(val)
        
        return len(nums)