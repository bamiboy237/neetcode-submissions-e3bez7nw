class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for parentheses in s:
            if stack and parentheses == ")" and stack[-1] == "(":
                stack.pop()
                continue
            stack.append(parentheses)
        return len(stack)

