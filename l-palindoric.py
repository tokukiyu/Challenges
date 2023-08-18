class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        
        # Initialize a table to store palindrome information
        dp = [[False] * n for _ in range(n)]
        start, max_length = 0, 1
        
        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check for palindromic substrings of length 2 
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2
        
        # Check for palindromic substrings of length >= 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # A substring is a palindrome if the inner substring is a palindrome
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if length > max_length:
                        start = i
                        max_length = length
        
        return s[start:start + max_length]
