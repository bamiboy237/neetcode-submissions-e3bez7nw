def evaluate(op1, op2, operator):
    if operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    elif operator == "*":
        return op1 * op2
    else:
        return int(op1 / op2)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                op2 = stack.pop()
                op1 = stack.pop()

                result = evaluate(op1, op2, token)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[-1]