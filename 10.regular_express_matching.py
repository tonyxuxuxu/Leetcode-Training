"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # When the pattern is None
        if not p:
            return not s
        # When the string is None, pattern like "a*" can still match it
        if not s and p:
            if 1 < len(p) and p[1] == "*":
                return self.isMatch(s, p[2:])
            else:
                return False
        # When the the second character of pattern is "*"
        if 1 < len(p) and p[1] == "*":
            # When the first character matches, there are three possible situation
            if s[0] == p[0] or p[0] == ".":
                return self.isMatch(s[1:], p) or \
                       self.isMatch(s[1:], p[2:]) or \
                       self.isMatch(s, p[2:])
            # Ignore the first two characters in pattern
            else:
                return self.isMatch(s, p[2:])
        else:
            if s[0] == p[0] or p[0] == ".":
                return self.isMatch(s[1:], p[1:])
            else:
                return False

if __name__ == '__main__':
    assert Solution().isMatch("aa", "aa*") is True