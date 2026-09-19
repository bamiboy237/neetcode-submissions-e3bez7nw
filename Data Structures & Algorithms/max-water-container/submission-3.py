class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        curr = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            max_amount = max(curr, max_amount)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_amount