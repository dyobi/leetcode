"836. Rectangle Overlap"

# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.
# Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.
# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3] / Output: true

# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1] / Output: false

# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1] / Output: false

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        x1 = rec1[0]
        x2 = rec1[2]
        y1 = rec1[1]
        y2 = rec1[3]

        x3 = rec2[0]
        x4 = rec2[2]
        y3 = rec2[1]
        y4 = rec2[3]

        return (x1 < x4 and y1 < y4 and x2 > x3 and y2 > y3) or (x3 < x2 and y3 < y2 and x4 > x1 and y4 > y1)
