class Matrix:
    def __init__(self, data):
        # Handle the empty matrix edge case
        if not data or not data[0]:
            self.data = []
            self.rows = 0
            self.cols = 0
            self.shape = (0, 0)
            return
        
        # Enforce uniform column lengths to prevent jagged matrices
        first_row_len = len(data[0])
        if any(len(row) != first_row_len for row in data):
            raise ValueError("All rows must have the same number of columns.")
            
        self.data = [list(row) for row in data]
        self.rows = len(self.data)
        self.cols = first_row_len
        self.shape = (self.rows, self.cols)
    
    def __repr__(self):
        if not self.data:
            return "Matrix(empty)"
            
        # Align all rows with consistent spacing
        rows_str = '\n  '.join(str(row) for row in self.data)
        return f"Matrix{self.shape}:\n  {rows_str}"