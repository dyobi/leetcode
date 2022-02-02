"557. Reverse Words in a String III"

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Input: s = "Let's take LeetCode contest" / Output: "s'teL ekat edoCteeL tsetnoc"

# Input: s = "God Ding" / Output: "doG gniD"

class Solution:
    def reverseWords(self, s: str) -> str:

        return ' '.join([i[::-1] for i in s.split(' ')])
