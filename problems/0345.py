"345. Reverse Vowels of a String"

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

# Input: s = "hello" / Output: "holle"
# Input: s = "leetcode" / Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        temp = []

        for i in range(len(s)):
            if s[i] in vowels:
                temp.append(s[i])

        temp[:] = temp[::-1]

        j = 0
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = temp[j]
                j += 1

        return "".join(s_list)
