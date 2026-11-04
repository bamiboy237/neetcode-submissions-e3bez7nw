class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        closed = 0
        
        for parenthesis in s:
            if parenthesis == "(":
                open_count += 1
            elif parenthesis == ")" and open_count > 0:
                open_count -= 1
            elif parenthesis == ")" and open_count == 0:
                closed += 1
                
        return closed  + open_count


