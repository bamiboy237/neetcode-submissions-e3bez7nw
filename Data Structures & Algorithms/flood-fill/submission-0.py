class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]

        if original == color:
            return image

        rows, cols = len(image), len(image[0])
        stack = [(sr, sc)]
        image[sr][sc] = color

        while stack:
            row, col = stack.pop()

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + dr
                next_col = col + dc

                in_bounds = (
                    0 <= next_row < rows and
                    0 <= next_col < cols
                )
                if in_bounds and image[next_row][next_col] == original:
                    image[next_row][next_col] = color
                    stack.append((next_row, next_col))

        return image