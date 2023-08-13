class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP array to store the number of unique paths at each cell
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the first row and column with 1, as there's only one way to reach them
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill in the DP array using the recurrence relation dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The value at dp[m-1][n-1] will contain the number of unique paths
        return dp[m-1][n-1]

# Example usage
solution = Solution()
m = 3
n = 7
print(solution.uniquePaths(m, n))  # Output: 6
