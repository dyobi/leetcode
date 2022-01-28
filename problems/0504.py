"504. Base 7"

# Given an integer num, return a string of its base 7 representation.

# Input: num = 100 / Output: "202"
# Input: num = -7 / Output: "-10"

class Solution:
    def convertToBase7(self, num: int) -> str:

        sign = res = ''

        if num == 0:
            return '0'

        if num < 0:
            sign = '-'
            num *= -1

        while num > 0:
            res = str(num % 7) + res
            num //= 7

        return sign + res
