class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int,
    ) -> List[List[int]]:
        original = image[sr][sc]

        # Recoloring to the same color would not change anything.
        if original == color:
            return image

        rows, cols = len(image), len(image[0])
        stack = [(sr, sc)]
        image[sr][sc] = color

        while stack:
            row, col = stack.pop()

            # Up
            if row - 1 >= 0 and image[row - 1][col] == original:
                image[row - 1][col] = color
                stack.append((row - 1, col))

            # Down
            if row + 1 < rows and image[row + 1][col] == original:
                image[row + 1][col] = color
                stack.append((row + 1, col))

            # Left
            if col - 1 >= 0 and image[row][col - 1] == original:
                image[row][col - 1] = color
                stack.append((row, col - 1))

            # Right
            if col + 1 < cols and image[row][col + 1] == original:
                image[row][col + 1] = color
                stack.append((row, col + 1))

        return image