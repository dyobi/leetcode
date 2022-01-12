"383. Ransom Note"

# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Input: ransomNote = "a", magazine = "b" / Output: false
# Input: ransomNote = "aa", magazine = "ab" / Output: false
# Input: ransomNote = "aa", magazine = "aab" / Output: true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        list_r = list(ransomNote)
        list_m = list(magazine)

        for i in list_r:
            if (i in list_m):
                list_m.remove(i)
            else:
                return False

        return True
