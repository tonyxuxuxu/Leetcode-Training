"""

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for __ in range(n)]
        isPal = [[False for __ in range(n)] for __ in range(n)]
        for i in range(n):
            m = i
            for j in range(i + 1):
                if s[j] == s[i] and (j + 1 > i - 1 or isPal[j + 1][i - 1]):
                    isPal[j][i] = True
                    m = 0 if j == 0 else min(m, dp[j - 1] + 1)
            dp[i] = m
        return dp[-1]