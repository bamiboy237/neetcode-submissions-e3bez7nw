class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heap[0]