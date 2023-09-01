from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        # Create a DP array to store the minimum path sums
        dp = triangle[-1] 
        

        # Traverse the triangle from bottom to top
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Calculate the minimum path sum for the current position
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        # The top of the dp array will now contain the minimum path sum
        return dp[0]