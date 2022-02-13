"605. Can Place Flowers"

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

# Input: flowerbed = [1,0,0,0,1], n = 1 / Output: true

# Input: flowerbed = [1,0,0,0,1], n = 2 / Output: false

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count, block = 0, 0

        for cur in flowerbed:

            if cur == 1:
                if block == 1:
                    count -= 1
                block = 1

            else:
                if block == 1:
                    block = 0
                else:
                    count += 1
                    block = 1

        return count >= n
