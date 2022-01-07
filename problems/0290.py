"290. Word Pattern"

# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Input: pattern = "abba", s = "dog cat cat dog" / Output: true
# Input: pattern = "abba", s = "dog cat cat fish" / Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s_dict = {}
        p_dict = {}
        
        if (len(s.split()) != len(pattern)) :
            return False
        
        for s, p in zip(s.split(), pattern) :
            s_dict[p] = s
            p_dict[s] = p
        
        return list(s_dict.keys()) == list(p_dict.values())