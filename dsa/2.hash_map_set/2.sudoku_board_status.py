class SudokuBoardStatus:
    def is_board_valid(self, matrix):
        #use hashsets to check if value in each row col is unique
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]

        #for subgrid, use '//' on rows and cols to check for unique nums in 9 subgrids of sudoku board
        sub_grid_set = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                #based on problem constraint
                if matrix[r][c] == 0:
                    continue
                #check if there are dups in rows, cols and reuturn False immediately if dups found
                if matrix[r][c] in row_set[r]:
                    return False
                if matrix[r][c] in col_set[c]:
                    return False
                #check each subgrid
                if matrix[r][c] in sub_grid_set[r // 3][c // 3]:
                    return False
                row_set[r].add(matrix[r][c])
                col_set[c].add(matrix[r][c])
                sub_grid_set[r // 3][c // 3].add(matrix[r][c])
        #only exits loop on not encountering dups at row, col and subgrid level
        return True

checker = SudokuBoardStatus()

valid_matrix = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print(f"Is the board valid? {checker.is_board_valid(valid_matrix)}")