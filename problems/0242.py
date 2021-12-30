"242. Valid Anagram"

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Input: s = "anagram", t = "nagaram" / Output: true
# Input: s = "rat", t = "car" / Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))