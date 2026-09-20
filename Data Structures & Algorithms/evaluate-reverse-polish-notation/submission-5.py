def evaluate(op1, op2, operator):
    if operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    elif operator == "*":
        return op1 * op2
    else:
        return  int(op1 / op2)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        evalu = 0

        for token in tokens:
            if stack and token in operators:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                evalu = evaluate(op1, op2, token)
                stack.append(evalu)
                continue
            stack.append(token)
        return int(stack[-1])
        