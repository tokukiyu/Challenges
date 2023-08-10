from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        # Initialize a DP array to store the minimum cost to reach each step.
        dp = [0] * n
        
        # Base cases: Cost to reach the first and second steps.
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Iterate through the rest of the steps and calculate the minimum cost.
        for i in range(2, n):
            # Minimum cost to reach the current step is the cost of the current step
            # plus the minimum of the cost to reach the previous step or the step before it.
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # The minimum cost to reach the top floor can be either from the last step or
        # the second to last step (since you can start from either step 0 or step 1).
        return min(dp[n-1], dp[n-2])

costs = [10, 15, 20]
sol=Solution()
# Call the function with the list of costs
result = sol.minCostClimbingStairs(costs)

# Print the result
print(result)
print(sol.minCostClimbingStairs(33))