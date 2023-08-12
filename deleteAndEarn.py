import collections
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Count the frequency of each number
        freq = collections.Counter(nums)
        
        # Find the maximum number in the input array
        max_num = max(nums)
        
        # Create a dynamic programming array to store the maximum points
        dp = [0] * (max_num + 1)
        dp[1] = freq[1] * 1
        
        # Calculate the maximum points for each number
        for num in range(2, max_num + 1):
            dp[num] = max(dp[num - 1], dp[num - 2] + freq[num] * num)
        
        # Return the maximum points        return dp[max_num]
    

# Example usage
nums = [3, 4, 2, 6]
solution = Solution()
print(solution.deleteAndEarn(nums))  # Output: 6
