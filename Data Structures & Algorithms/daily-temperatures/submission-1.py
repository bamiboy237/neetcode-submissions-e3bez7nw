class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        for i in range(len(temperatures)):
            while result[n:] and temperatures[i] > temperatures[result[-1]]:
                index = result.pop()
                result[index] = i - index
            result.append(i)

        while len(result) > n:
            result.pop()

        return result
