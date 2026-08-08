from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        right = 0

        while right < len(nums):
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            while dq[0] <= right - k:
                dq.popleft()

            

            if right >= k - 1:
                result.append(nums[dq[0]])
            right += 1
        return result 