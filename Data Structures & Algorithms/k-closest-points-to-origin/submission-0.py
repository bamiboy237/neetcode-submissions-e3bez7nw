from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean(x1, y1) -> float:
            return sqrt((x1 ** 2) + (y1 ** 2))

        heap = [(euclidean(x, y), [x, y]) for x, y in points]

        heapq.heapify(heap)
        result = []

        for _ in range(k):
            pt, point = heapq.heappop(heap)
            result.append(point)

        return result

        