"231. Power of Two"

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Input: n = 16 / Output: true
# Explanation: 24 = 16

# Input: n = 3 / Output: false

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not (n & n - 1)