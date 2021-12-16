"171. Excel Sheet Column Number"

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
# Input: columnTitle = "ZY" / Output: 701

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        str = columnTitle[::-1]
        res = 0
        t = 1
        
        for i in range(len(str)) :
            res = res + t * (ord(str[i]) - 64)
            t *= 26
        
        return res