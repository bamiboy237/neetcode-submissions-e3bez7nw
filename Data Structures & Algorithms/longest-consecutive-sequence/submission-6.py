import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        heapq.heapify(nums)

        prev = heapq.heappop(nums)
        max_len = 1
        running_len = 1

        while nums:
            if nums[0] == prev:
                heapq.heappop(nums)

            elif nums[0] == prev + 1:
                prev = heapq.heappop(nums)
                running_len += 1
                max_len = max(max_len, running_len)

            else:
                prev = heapq.heappop(nums)
                running_len = 1

        return max_len