"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p_index, s_index, last_s_index, last_p_index = 0, 0, -1, -1
        while s_index < len(s):
            # Normal match including '?'
            if p_index < len(p) and (s[s_index] == p[p_index] or p[p_index] == '?'):
                s_index += 1
                p_index += 1
            # Match with '*'
            elif p_index < len(p) and p[p_index] == '*':
                p_index += 1
                last_s_index = s_index
                last_p_index = p_index
            # Not match, but there is a '*' before
            elif last_p_index != -1:
                last_s_index += 1
                s_index = last_s_index
                p_index = last_p_index
            # Not match and there is no '*' before
            else:
                return False
        # Check if there is still character except '*' in the pattern
        while p_index < len(p) and p[p_index] == '*':
            p_index += 1
        # If finish scanning both string and pattern, then it matches well
        return p_index == len(p)
