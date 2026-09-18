import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heap = nums.copy()
        if not heap:
            return 0

        heapq.heapify(heap)

        prev = heapq.heappop(heap)
        max_len = 1
        running_len = 1

        while heap:
            if heap[0] == prev:
                heapq.heappop(heap)

            elif heap[0] == prev + 1:
                prev = heapq.heappop(heap)
                running_len += 1
                max_len = max(max_len, running_len)

            else:
                prev = heapq.heappop(heap)
                running_len = 1

        return max_len