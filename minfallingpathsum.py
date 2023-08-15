class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        # Initialize a DP table to store minimum falling path sums
        dp = [[0] * n for _ in range(n)]
        
        # Initialize the first row of DP table with the values from the matrix
        for col in range(n):
            dp[0][col] = matrix[0][col]
        
        # Iterate over each row and calculate the minimum falling path sum
        for row in range(1, n):
            for col in range(n):
                # Calculate the possible paths and select the minimum
                dp[row][col] = matrix[row][col] + min(
                    dp[row - 1][col],                 # Directly below
                    dp[row - 1][max(col - 1, 0)],    # Diagonally left
                    dp[row - 1][min(col + 1, n - 1)] # Diagonally right
                )
        
        # Return the minimum falling path sum from the last row
        return min(dp[n - 1])
