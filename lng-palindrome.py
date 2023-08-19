class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        # Create a 2D DP table to store the lengths of palindromic subsequences
        dp = [[0] * n for _ in range(n)]
        
        # All characters are palindromic subsequences of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the DP table using bottom-up approach
        for cl in range(2, n+1):  # cl is the length of the subsequence
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j] and cl == 2:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        
        # The top-right corner of the DP table contains the longest palindromic subsequence's length
        return dp[0][n-1]
