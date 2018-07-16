"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
"""

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        s_length = len(s)
        word_num = len(words)
        word_length = len(words[0])
        word_lengths = word_num * word_length
        result = []
        word_dicts = {}
        for word in words:
            word_dicts[word] = word_dicts[word] + 1 if word in word_dicts else 1
        for i in range(s_length):
            left = right = i
            curr_dicts = {}
            while right + word_length <= s_length:
                word = s[right:right + word_length]
                right += word_length
                if word in word_dicts:
                    curr_dicts[word] = curr_dicts[word] + 1 if word in curr_dicts else 1
                    while curr_dicts[word] > word_dicts[word]:
                        curr_dicts[s[left:left + word_length]] -= 1
                        left += word_length
                    if right - left == word_length:
                        result.append(left)
                else:
                    curr_dicts.clear()
                    left = right
            return result


if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    sol = Solution()
    print(sol.findSubstring(s, words))