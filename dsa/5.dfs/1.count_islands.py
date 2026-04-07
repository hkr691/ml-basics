class CountIslands:

  def count_islands(self, grid):
  
    row, col = len(grid), len(grid[0])
    visited = set()    #can be optimized for constant space by marking visited cells to 0 without a need for set
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    
    def dfs(r, c):
    
      if (r, c) in visited:
        return
      if r < 0 or r >= row or c < 0 or c >= col:
        return
      if grid[r][c] != 1:
        return
      
      visited.add((r, c))
      for dirs in directions:
        dfs(r+dirs[0], c+dirs[1])
    
    for r in range(row):
      for c in range(col):
        if grid[r][c] == 1 and (r, c) not in visited:
          dfs(r, c)
          count += 1
    return count
      
    
