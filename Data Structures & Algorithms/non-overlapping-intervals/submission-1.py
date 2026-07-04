class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort(key = lambda x: x[1])
        lastKept = intervals[0][1]
        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < lastKept:
                count += 1
            else:
                lastKept = intervals[i][1]
        
        return count