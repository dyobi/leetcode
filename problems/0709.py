"709. To Lower Case"

# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

# Input: s = "Hello" / Output: "hello"
# Input: s = "here" / Output: "here"
# Input: s = "LOVELY" / Output: "lovely"

class Solution:
    def toLowerCase(self, s: str) -> str:

        res = ''

        for c in s:
            if (ord(c) > 64 and ord(c) < 91):
                res += chr(ord(c) + 32)
            else:
                res += c

        return res
