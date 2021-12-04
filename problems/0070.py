"70. Climbing Stairs"

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Input: n = 3 / Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step / 2. 1 step + 2 steps / 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        x, y, res = 0, 1, 1
        for i in range(n) :
            res = x + res
            x = y
            y = res
        return res
        