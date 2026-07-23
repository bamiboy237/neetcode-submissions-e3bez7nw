class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda a, b: b + a,
            "-": lambda a, b: b - a,
            "*": lambda a, b: b * a,
            "/": lambda a, b: int(b / a)
        }
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(operators[token](a, b))

        return stack[0]