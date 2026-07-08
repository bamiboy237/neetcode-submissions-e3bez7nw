class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0

        left, right = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        results = 0

        while left < right:
            if height[left] < height[right]:
                maxLeft = max(maxLeft, height[left])
                results += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                results  += maxRight - height[right]
                right -= 1

        return results