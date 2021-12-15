"169. Majority Element"

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        from collections import Counter

        dic = Counter(nums)

        for key, val in dic.items():
            if val > len(nums)/2:
                return key
