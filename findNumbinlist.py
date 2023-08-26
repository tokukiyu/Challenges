class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lengths = [1] * n  # Length of longest increasing subsequence ending at index i
        counts = [1] * n   # Count of longest increasing subsequences ending at index i
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[i] == lengths[j] + 1:
                        counts[i] += counts[j]
                    elif lengths[i] < lengths[j] + 1:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
            
        max_length = max(lengths)
        result = 0
        for i in range(n):
            if lengths[i] == max_length:
                result += counts[i]
        
        return result
