from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # Initialize a 2D DP array to store the number of paths at each cell
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the starting cell
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        # Populate the first row (robot can only move right)
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0
        
        # Populate the first column (robot can only move down)
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0
        
        # Populate the rest of the DP array
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]

# Example usage
obstacleGrid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))  # Output should be 2
