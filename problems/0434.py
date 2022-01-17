"434. Number of Segments in a String"

# Given a string s, return the number of segments in the string.
# A segment is defined to be a contiguous sequence of non-space characters.

# Input: s = "Hello, my name is John" / Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

# Input: s = "Hello" / Output: 1

class Solution:
    def countSegments(self, s: str) -> int:

        return len(s.split())
