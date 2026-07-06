class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if not intervals or n == 1:
            return intervals

        intervalsSorted = sorted(intervals, key = lambda x: x[0])
        result = [intervalsSorted[0][:]]

        for i in range(1, n):
            if intervalsSorted[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervalsSorted[i][1])
            else:
                result.append(intervalsSorted[i][:])
                

        return result