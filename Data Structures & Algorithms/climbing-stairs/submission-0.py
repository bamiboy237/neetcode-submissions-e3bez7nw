class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        prev_prev = 1
        prev = 1
        for i in range(2, n+1):
            curr = prev_prev + prev
            prev_prev = prev
            prev = curr

        return prev