"459. Repeated Substring Pattern"

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# Input: s = "abab" / Output: true
# Explanation: It is the substring "ab" twice.

# Input: s = "aba" / Output: false

# Input: s = "abcabcabcabc" / Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        slen = len(s)

        for i in range(1, (slen//2) + 1):
            if (s[0] == s[i] and slen % i == 0 and (s[:i] * (slen//i)) == s):
                return True

        return False
