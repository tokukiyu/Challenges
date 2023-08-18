from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # Create a set for faster word lookup
        word_set = set(wordDict)
        
        # dp[i] will be True if s[:i] can be segmented into words from wordDict
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is always in the wordDict
        
        for i in range(1, n + 1):
            for j in range(i):
                # Check if the current substring can be segmented
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
    
solution = Solution()
s = "leetcode" 
wordDict = ["leet", "code"]
print(solution.wordBreak(s, wordDict))  # Output: True

s = "applepenapple"
wordDict = ["apple", "pen"]
print(solution.wordBreak(s, wordDict))  # Output: True

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(solution.wordBreak(s, wordDict))  # Output: False
 