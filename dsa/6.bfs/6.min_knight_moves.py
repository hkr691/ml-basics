"""
You are given a chessboard of infinite size where the coordinates of each cell are defined by integer pairs (x, y). The knight piece moves in an L-shape, either two squares horizontally and one square vertically, or two squares vertically and one square horizontally.

Write a function to determine the minimum number of moves required for the knight to move from the starting position (0, 0) to the target position (x, y). Assume that it is always possible to reach the target position, and that x and y are both integers in the range [-200, 200]
"""

from collections import deque

class MinKnightMoves:
  def solution(self, x: int, y: int) -> int:
    queue = deque([(0 ,0 ,0)])
    visited = set([(0, 0)])
    dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    while queue:
      cx, cy, moves = queue.popleft()
      
      if (cx, cy) == (x, y):
        return moves
      
      for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if nx, ny not in visited:
          queue.append((nx, ny, moves + 1))
          visited.add(nx, ny)
    return -1
      
