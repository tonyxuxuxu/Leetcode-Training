"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.dfs(0, s, [], result)
        return result

    def dfs(self, length, s, ips, result):
        if not s:
            if length == 4:
                result.append('.'.join(ips))
            return
        elif length == 4:
            return

        self.dfs(length+1, s[1:], ips+[s[:1]], result)

        if s[0] != '0':
            if len(s) >= 2:
                self.dfs(length+1, s[2:], ips+[s[:2]], result)
            if len(s) >= 3 and int(s[:3]) <= 255:
                self.dfs(length+1, s[3:], ips+[s[:3]], result)


if __name__ == '__main__':
    sol = Solution()
    ip = "25525511135"
    print(sol.restoreIpAddresses(ip))
