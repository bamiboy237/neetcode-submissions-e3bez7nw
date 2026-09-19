class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for parentheses in s:
            if parentheses in pairs:
                if not stack or stack[-1] != pairs[parentheses]:
                    return False
                stack.pop()
            else:
                stack.append(parentheses)
        
        return len(stack) == 0