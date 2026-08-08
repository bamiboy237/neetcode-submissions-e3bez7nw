class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = maxRight = -1
        trapped = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])

            if maxLeft < maxRight:
                depth = maxLeft - height[left]
                trapped += depth
                left += 1
            else:
                depth = maxRight - height[right]
                trapped += depth
                right -= 1

        return trapped