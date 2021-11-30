"69. Sqrt(x)"

# Input: x = 8 / Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 0
        right = x
        
        if x == 0 or x == 1 :
            return x
        else :
            while left + 1 != right :
                mid = int((left + right) / 2)
                val = mid*mid
                if val == x :
                    return mid
                elif val < x :
                    left = mid
                elif val > x :
                    right = mid
        
        return left