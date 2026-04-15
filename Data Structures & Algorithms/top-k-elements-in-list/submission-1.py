class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        num_count = []
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        for num, count in counts.items():
            num_count.append((-count, num))
        heapq.heapify(num_count)
        top_k = []
        for i in range(k):
            top_k.append((heapq.heappop(num_count))[1])
        return top_k
