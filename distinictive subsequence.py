class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # Initialize a 2D DP array to store the counts
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # When t is an empty string, there's exactly one subsequence in s (empty string)
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill the DP array using bottom-up approach
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]
# Example usage
solution = Solution()
s = "rabbbit"
t = "rabbit"
print(solution.numDistinct(s, t))  # Output: 3
