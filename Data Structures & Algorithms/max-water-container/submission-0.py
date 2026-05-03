class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        current_max = 0
        
        while left < right:
            width = right - left
            height = min(heights[right], heights[left])

            current_area = width * height
            current_max = max(current_area, current_max)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return current_max