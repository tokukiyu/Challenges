from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Create a 2D DP array to store the minimum sum at each cell
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the first row and column
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Fill in the DP array using the recurrence relation dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        # The value at dp[m-1][n-1] will contain the minimum path sum
        return dp[m-1][n-1]

# Example usage
solution = Solution()
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(solution.minPathSum(grid))  # Output: 7
