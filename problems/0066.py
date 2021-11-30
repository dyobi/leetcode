"66. Plus One"

# Input: digits = [1,2,3] / Output: [1,2,4]
# Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus, the result should be [1,2,4].

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list((str)((int)(''.join(map(str, digits)))+1))