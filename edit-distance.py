class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        # Create a 2D DP array to store the minimum operations needed for each substring
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the first row and column
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # Fill in the DP array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # No operation needed
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
        return dp[m][n]

# Example usage
solution = Solution()
word1 = "horse"
word2 = "ros"
print(solution.minDistance(word1, word2))  # Output: 3
