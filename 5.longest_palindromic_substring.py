"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = end = 0
        for i in range(len(s)):
            maxlensodd = self.longestPalindromeFromMiddle(i, i, s)
            maxlenseven = self.longestPalindromeFromMiddle(i, i+1, s)
            maxlen = max(maxlensodd, maxlenseven)
            if maxlen > end - start:
                start = int(i - (maxlen)/2 + 1)
                end = int(i + maxlen/2 + 1)
        return s[start: end]

    def longestPalindromeFromMiddle(self, left, right, string):
        str_lens = len(string)
        while left >= 0 and right < str_lens and string[left] == string[right]:
            left -= 1
            right += 1
        return right-left-1


if __name__ == '__main__':
    sol = Solution()
    input = 'cbbd'
    output = sol.longestPalindrome(input)
    print(output)
