class ZeroStriping:
    def zero_stripe_matrix(self, matrix):
        if not matrix or not matrix[0]: return
        m, n = len(matrix), len(matrix[0])
        
        # Capture original state of first row/col BEFORE marking
        row0_zero = any(matrix[0][c] == 0 for c in range(n))
        col0_zero = any(matrix[r][0] == 0 for r in range(m))

        # first pass - row/col to mark zeros for the rest of the matrix
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        # second pass - Use those markers to update the matrix (inner part)
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # Finally, handle the first row and column based on initial flags to have matrix modified in place
        if row0_zero:
            for c in range(n): matrix[0][c] = 0
        if col0_zero:
            for r in range(m): matrix[r][0] = 0

striper = ZeroStriping()

matrix1 = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12]
]
striper.zero_stripe_matrix(matrix1)
print(matrix1)
