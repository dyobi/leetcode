"476. Number Complement"

# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.

# Input: num = 5 / Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

# Input: num = 1 / Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

class Solution:
    def findComplement(self, num: int) -> int:

        s = bin(num)[2::]

        s_c = s.replace("1", "a")
        s_c = s_c.replace("0", "1")
        s_c = int(('0b' + s_c.replace("a", "0")), 2)

        return s_c
