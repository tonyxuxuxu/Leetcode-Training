"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        charMap = {}
        for i in range(256):
            charMap[i] = -1
        ls = len(s)
        i = max_len = 0
        for j in range(ls):
            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1
            charMap[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
        return max_len

if __name__ == '__main__':
    sol = Solution()
    str = "abcabcbb"
    print(sol.lengthOfLongestSubstring(str))