"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution1:

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

class Solution2:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sls = len(set(s))
        lens = len(s)
        if lens >= 1:
            max_lens = 1
        else:
            return 0

        for i in range(lens):
            for j in range(i+max_lens+1, i+sls+1):
                curr = s[i:j]
                curr_lens = len(curr)
                if len(set(curr)) != curr_lens:
                    break
                else:
                    if curr_lens > max_lens:
                        max_lens = curr_lens
        return max_lens

if __name__ == '__main__':
    str = "abcabcbb"
    sol1 = Solution1()
    print(sol1.lengthOfLongestSubstring(str))
    sol2 = Solution2()
    print(sol2.lengthOfLongestSubstring(str))
