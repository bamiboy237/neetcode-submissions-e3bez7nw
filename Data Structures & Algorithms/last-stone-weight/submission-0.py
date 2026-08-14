class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.arr = [-x for x in stones]
        heapq.heapify(self.arr)

        while len(self.arr) > 1:
            x = -heapq.heappop(self.arr)
            y = -heapq.heappop(self.arr)

            if x != y:
                heapq.heappush(self.arr, - (x - y))

        return 0 if not self.arr else -heapq.heappop(self.arr)
            