# # You are climbing a staircase. It takes n steps to reach the top.# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1  # One way to reach step 1
        dp[2] = 2  # Two ways to reach step 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
solution = Solution()

# Call the climbStairs function and print the result
n = 5  # Replace this with the desired number of steps
result = solution.climbStairs(n)
print(f"Number of distinct ways to climb {n} steps: {result}")