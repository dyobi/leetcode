"167. Two Sum II - Input Array Is Sorted"

# Input: numbers = [2,7,11,15], target = 9 / Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            rem = target - numbers[i]
            if (rem in numbers[:i:-1]):
                return [i+1, numbers[i+1::].index(rem)+i+2]
        return []
