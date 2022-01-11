"350. Intersection of Two Arrays II"

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Input: nums1 = [1,2,2,1], nums2 = [2,2] / Output: [2,2]
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4] / Output: [4,9]
# Explanation: [9,4] is also accepted.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []

        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                res.append(i)

        return res
