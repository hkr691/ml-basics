from typing import List

class Solution:
    def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Your code goes here
        if not image or not image[0]:
            return image
        
        original = image[sr][sc]
        if original == color:
            return image
        
        rows, cols = len(image), len(image[0])
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs_helper(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original:
                return
            
            image[r][c] = color
            visited.add((r, c))

            for dr, dc in dirs:
                dfs_helper(r + dr, c + dc)
        
        dfs_helper(sr, sc)
        return image
        

