"""You'll implement this."""

from collections import deque
from typing import List, Optional

from maze import Maze, Position, CellType


class Solver:
    def __init__(self, maze: Maze) -> None:
        self.maze = maze

    def _is_valid_directional_move(self, from_pos: Position, to_pos: Position) -> bool:
        """Check if movement from from_pos to to_pos respects directional constraints."""
        from_cell = self.maze.get_cell(from_pos)
        
        # Calculate direction of movement
        row_diff = to_pos.row - from_pos.row
        col_diff = to_pos.col - from_pos.col
        
        # If moving from a RIGHT_ONLY cell, can only move right
        if from_cell == CellType.RIGHT_ONLY.value:
            return col_diff == 1 and row_diff == 0
        
        # If moving from a LEFT_ONLY cell, can only move left
        if from_cell == CellType.LEFT_ONLY.value:
            return col_diff == -1 and row_diff == 0
        
        # For all other cell types, movement is unrestricted
        return True

    def solve(self) -> Optional[List[Position]]:
        start = self.maze.get_start()
        end = self.maze.get_end()
        
        # BFS queue: each element is (current_position, path_to_current_position)
        queue = deque([(start, [start])])
        visited = {start}
        
        while queue:
            current_pos, path = queue.popleft()
            
            # Check if we reached the end
            if self.maze.is_end(current_pos):
                return path
            
            # Explore all valid neighbors
            for neighbor in self.maze.get_neighbors(current_pos):
                if neighbor not in visited and self._is_valid_directional_move(current_pos, neighbor):
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))
        
        # No path found
        return None