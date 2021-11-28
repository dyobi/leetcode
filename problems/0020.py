"20. Valid Parentheses"

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Input: s = "([)]" / Output: false
# Input: s = "()[]{}" / Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        while ("{}" in s or "[]" in s or "()" in s) :
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            s = s.replace("()", "")
        return True if s == "" else False