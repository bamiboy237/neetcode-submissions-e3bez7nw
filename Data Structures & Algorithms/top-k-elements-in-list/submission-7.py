import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        heap = []

        for key, value in hashmap.items():
            heapq.heappush(heap, (-value, key))

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
