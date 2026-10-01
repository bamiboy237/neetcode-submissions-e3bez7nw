from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        neighbor_pos = ((-1, 0), (1, 0), (0, -1), (0, 1))

        rottens = []
        minutes = 0
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    rottens.append((row, col))

        queue = deque(rottens)
        while queue and fresh > 0:
            patch_size = len(queue)
            for _ in range(patch_size):
                rot_row, rot_col = queue.popleft()
                for dr, dc in neighbor_pos:
                    r, c = rot_row + dr, rot_col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append((r, c))
            minutes += 1
        
        return minutes if fresh == 0 else -1
