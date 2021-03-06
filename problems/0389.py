"389. Find the Difference"

# You are given two strings s and t.
# String t is generated by random shuffling string s and then add one more letter at a random position. Return the letter that was added to t.

# Input: s = "abcd", t = "abcde" / Output: "e"
# Explanation: 'e' is the letter that was added.
# Input: s = "", t = "y" / Output: "y"

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        lst_s = list(s)
        lst_t = list(t)

        for i in lst_s:
            if i in lst_t:
                lst_t.remove(i)

        return "".join(lst_t)
