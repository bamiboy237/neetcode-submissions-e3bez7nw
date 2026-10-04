class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()
        word_len = len(word)
        count = 0
        def backtrack(r, c, count):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if (r, c) in seen or board[r][c] != word[count]:
                    return False

            if count == word_len - 1:
                        return True
                        
            seen.add((r, c))
            found = (backtrack((r + 1), c, count + 1) or backtrack((r - 1), c, count + 1) or backtrack(r, c+1, count + 1) or backtrack(r, c-1, count+1))

            seen.remove((r, c))
            return found

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        return False

                    

