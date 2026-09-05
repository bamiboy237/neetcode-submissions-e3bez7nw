import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = []
        for i in nums:
            heapq.heappush(temp, -i)

        for _ in range(1,k):
            heapq.heappop(temp)

        result = -heapq.heappop(temp)
        return result