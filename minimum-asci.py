class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Initialize a 2D DP table to store the minimum ASCII sum
        # required to make substrings s1[:i] and s2[:j] equal.
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        # Fill in the DP table using bottom-up dynamic programming
        for i in range(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
        
        for j in range(len(s2) - 1, -1, -1):
            dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])
        
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(ord(s1[i]) + dp[i+1][j], ord(s2[j]) + dp[i][j+1])
        
        return dp[0][0]  # The answer is stored in the top-left corner of the DP table
 
 
# Example usage
solution = Solution()
s1 = "sea"
s2 = "eat"
result = solution.minimumDeleteSum(s1, s2)
print(result)  # Output: 231
