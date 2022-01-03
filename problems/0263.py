"263. Ugly Number"

# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.

# Input: n = 6 / Output: true
# Explanation: 6 = 2 × 3

class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n == 1 :
            return True
        else :
            divider = [2, 3, 5]
            i = 0
            
            while (n > 1 and i < len(divider)) :
                if n % divider[i] == 0 :
                    n = n // divider[i]
                else :
                    i += 1
        
        return n == 1