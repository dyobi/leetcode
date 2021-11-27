"1. Two Sum"

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)) :
            rest = target - nums[i]
            if (rest in nums and nums.index(rest) != i) :
                return [i, nums.index(rest)]