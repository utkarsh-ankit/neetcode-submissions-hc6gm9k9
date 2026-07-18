class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Step 1: Transpose across the main diagonal
        for i in range(n):
            # Only loop from i + 1 to n to swap each pair once!
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # Step 2: Flip horizontally (reverse every row)
        for i in range(n):
            matrix[i].reverse()