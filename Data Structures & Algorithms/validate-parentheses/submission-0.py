class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for parentheses in s:
            if parentheses in mapping:
                if not stack or stack[-1] != mapping[parentheses]:
                    return False
                stack.pop()
            else:
                stack.append(parentheses)
        
        return len(stack) == 0