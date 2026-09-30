class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [[] for _ in range(numRows)]
        row = 0
        step = 1

        for char in s:
            rows[row].append(char)

            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            row += step
        return "".join("".join(chars) for chars in rows)