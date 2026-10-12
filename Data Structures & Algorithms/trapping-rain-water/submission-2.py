class Solution:
	def trap(self, height: List[int]) -> int:
		max_left = max_right = -1
		left, right = 0, len(height) - 1

		trapped = 0

		while left < right:
			max_left = max(max_left, height[left])
			max_right = max(max_right, height[right])

			if max_left <= max_right:
				depth = max_left - height[left]
				trapped += depth
				left += 1
			else:
				depth = max_right - height[right]
				trapped += depth
				right -= 1
		return trapped
