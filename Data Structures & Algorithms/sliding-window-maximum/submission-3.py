from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        right = 0

        while right < len(nums):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            while dq and dq[0] < right - k + 1:
                dq.popleft()

            dq.append(right)

            if right >= k - 1:
                result.append(nums[dq[0]])
            right += 1
        return result 