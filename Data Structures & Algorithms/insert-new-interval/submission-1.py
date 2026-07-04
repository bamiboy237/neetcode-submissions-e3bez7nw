class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        if i == len(intervals):
            result.append(newInterval)
            return result

        tempNewInterval = newInterval.copy()
        tempNewInterval[0] = min(intervals[i][0], tempNewInterval[0])
        while i < len(intervals) and tempNewInterval[1] >= intervals[i][0]:
            tempNewInterval[1] = max(intervals[i][1], tempNewInterval[1])
            i += 1

        result.append(tempNewInterval)
        result.extend(intervals[i:])

        return result
