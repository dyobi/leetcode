"258. Add Digits"

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Input: num = 38 / Output: 2 / Explanation: The process is 38 --> 3 + 8 --> 11 && 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
# Input: num = 0 / Output: 0

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10 : return num
        
        res = 0
        while (num >= 10) :
            res += num % 10
            num = num//10
        res = res + num
        
        return self.addDigits(res)