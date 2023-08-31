from typing import List
class Solution:
    def findLongestChain(self, pairs: List [List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  # Sort pairs based on the second element
        
        dp = [1] * len(pairs)  
        
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)  # Return the maximum value in the dp array
