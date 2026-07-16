class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                earlier_index = stack.pop()
                answers[earlier_index] = i - earlier_index
            stack.append(i)

        return answers