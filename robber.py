from typing import List
class Solution:
    def rob(self, nums: List[int]) ->int:
        n=len(nums)
        oddprt=nums[1::2]
        evenprt=nums[0::2]
        
        if sum(oddprt)>=sum(evenprt):
            return sum(oddprt)
        else:
            return sum(evenprt)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        # Initialize an array to store the maximum amount of money that can be robbed
        dp = [0] * n
        
        # Base cases for the first two houses
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Iterate through the rest of the houses
        for i in range(2, n):
            # Choose whether to rob the current house or not
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        # The last element of dp will hold the maximum amount of money that can be robbed
        return dp[n - 1]
