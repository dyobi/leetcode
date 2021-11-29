"58. Length of Last Word"

# Input: s = "Hello World" / Output: 5
# Explanation: The last word is "World" with length 5.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[len(s.split()) - 1])