"806. Number of Lines To Write String"

# You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

# You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this process until you have written all of s.

# Return an array result of length 2 where:

# result[0] is the total number of lines.
# result[1] is the width of the last line in pixels.

# Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz" / Output: [3,60]
# Explanation: You can write s as follows:
# abcdefghij  // 100 pixels wide
# klmnopqrst  // 100 pixels wide
# uvwxyz      // 60 pixels wide
# There are a total of 3 lines, and the last line is 60 pixels wide.

# Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa" / Output: [2,4]
# Explanation: You can write s as follows:
# bbbcccdddaa  // 98 pixels wide
# a            // 4 pixels wide
# There are a total of 2 lines, and the last line is 4 pixels wide.

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        rows = 0
        pixel = 0

        for c in s:

            if pixel + widths[ord(c) - 97] <= 100:
                pixel += widths[ord(c) - 97]
            else:
                pixel = widths[ord(c) - 97]
                rows += 1

        return [rows + 1, pixel]
