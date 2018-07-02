"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows<=1:
            return s
        result = ''
        index = 0
        n = len(s)
        for i in range(0, numRows):
            if i == 0 or i == numRows - 1:
                while index < n:
                    result += s[index]
                    index += 2 * numRows - 2
                index = i + 1
            else:
                while index < n:
                    result += s[index]
                    index += 2 * numRows - 2 * i - 2
                    if index >= n:
                        break
                    result += s[index]
                    index += 2 * i
                index = i + 1
        return result


if __name__ == '__main__':
    sol = Solution()
    s = "PAYPALISHIRING"
    print(sol.convert(s, 3))
