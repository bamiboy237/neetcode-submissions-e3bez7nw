class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n == 1:
            return 0

        intervals.sort(key = lambda x: x[1])
        lastKept = intervals[0][1]
        count = 0

        for i in range(1, n):
            if intervals[i][0] < lastKept:
                count += 1
            else:
                lastKept = intervals[i][1]
        
        return count