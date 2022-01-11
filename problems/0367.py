"367. Valid Perfect Square"

# Given a positive integer num, write a function which returns True if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.

# Input: num = 16 / Output: true
# Input: num = 14 / Output: false

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num

        if num == 1:
            return True

        while (left < right):
            mid = (right + left) // 2
            mid_pow = mid**2

            if (mid_pow < num):
                left += 1
            elif (mid_pow > num):
                right = mid
            elif (mid_pow == num):
                break

        return left != right
