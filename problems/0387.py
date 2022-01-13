"387. First Unique Character in a String"

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Input: s = "leetcode" / Output: 0
# Input: s = "loveleetcode" / Output: 2
# Input: s = "aabb" / Output: -1

class Solution:
    def firstUniqChar(self, s: str) -> int:

        for i in range(len(s)):
            if (s.count(s[i]) == 1):
                return i

        return -1
