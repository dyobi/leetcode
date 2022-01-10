"344. Reverse String"

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Input: s = ["h","e","l","l","o"] / Output: ["o","l","l","e","h"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s[:] = s[::-1]