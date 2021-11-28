"9. Palindrome Number"

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1] :
            return True
        else :
            return False