from typing import List

class Solution:
    def surrounded_regions(self, grid: List[List[str]]) -> List[List[str]]:
        # Your code goes here
        if not grid:
            return grid
        
        rows, cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != 'O':
                return
            grid[r][c] = 'S'
            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        
        for c in range(cols):
            if grid[0][c] == 'O':
                dfs(0, c)
            if grid[rows - 1][c] == 'O':
                dfs(rows - 1, c)
        
        for r in range(rows):
            if grid[r][0] == 'O':
                dfs(r, 0)
            if grid[r][cols - 1] == 'O':
                dfs(r, cols - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'
                if grid[r][c] == 'S':
                    grid[r][c] = 'O'
        return grid

grid = [
["X","X","X","X","O"],
["X","X","O","X","X"],
["X","X","O","X","O"],
["X","O","X","X","X"],
["X","O","X","X","X"]
]

"""
expected output
[
["X","X","X","X","O"],
["X","X","X","X","X"],
["X","X","X","X","O"],
["X","O","X","X","X"],
["X","O","X","X","X"]
]
"""

soln = Solution()
print(soln.surrounded_regions(grid))
