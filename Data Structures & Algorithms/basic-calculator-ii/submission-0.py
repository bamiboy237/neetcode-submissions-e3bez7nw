class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(num1, num2, operator):
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                return int(num1 / num2)

        precedence = {
            "*": 2,
            "/": 2,
            "+": 1,
            "-": 1
        }

        nums = []
        ops = []
        temp = 0

        for char in s:
            if char.isdigit():
                temp = temp * 10 + int(char)

            elif char in precedence:
                nums.append(temp)
                temp = 0

                while ops and precedence[ops[-1]] >= precedence[char]:
                    op = ops.pop()
                    num2 = nums.pop()
                    num1 = nums.pop()
                    nums.append(evaluate(num1, num2, op))

                ops.append(char)

        nums.append(temp)

        while ops:
            op = ops.pop()
            num2 = nums.pop()
            num1 = nums.pop()
            nums.append(evaluate(num1, num2, op))

        return nums[0]