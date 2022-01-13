"392. Is Subsequence"

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Input: s = "abc", t = "ahbgdc" / Output: true
# Input: s = "axc", t = "ahbgdc" / Output: false

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        lst_s = list(s)
        lst_t = list(t)

        i = 0

        for j in list(t):
            if i < len(s) and j == lst_s[i]:
                i += 1
            else:
                del lst_t[i]

        return lst_s == lst_t
