"500. Keyboard Row"

# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# Input: words = ["Hello","Alaska","Dad","Peace"] / Output: ["Alaska","Dad"]
# Input: words = ["omk"] / Output: []
# Input: words = ["adsdf","sfd"] / Output: ["adsdf","sfd"]

class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        f_row = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        s_row = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        t_row = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])

        res = []

        for i in words:
            tmp = set(i.lower())

            if not (tmp - f_row) or not (tmp - s_row) or not (tmp - t_row):
                res.append(i)
        return res
