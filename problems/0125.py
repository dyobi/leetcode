"125. Valid Palindrome"

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Input: s = "A man, a plan, a canal: Panama" / Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        import re
        
        res = re.sub('[^a-zA-Z0-9]', '', s).lower()
        
        return True if res == res[::-1] else False