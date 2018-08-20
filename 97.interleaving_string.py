"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        length1 = len(s1)
        length2 = len(s2)
        length3 = len(s3)
        if length1 + length2 != length3:
            return False
        dp = [[True for _ in range(length2 + 1)] for _ in range(length1 + 1)]
        for i in range(1, length1 + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, length2 + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or \
                           (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
        return dp[-1][-1]