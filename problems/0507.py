"507. Perfect Number"

# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
# Given an integer n, return true if n is a perfect number, otherwise return false.

# Input: num = 28 / Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.

# Input: num = 7 / Output: false

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        res = 0

        for i in range(1, int(sqrt(num)) + 1):
            if num % i == 0:
                res += i
                if num // i != i:
                    res += num // i

        return res == 2*num
