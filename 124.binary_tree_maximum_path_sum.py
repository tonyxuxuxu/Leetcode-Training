"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        self._maxPathSum(root)
        return self.res

    def _maxPathSum(self, node):
        if not node:
            return 0
        left = self._maxPathSum(node.left)
        right = self.maxPathSum(node.right)
        left = left if left > 0 else 0
        right = right if right > 0 else 0
        self.res = max(self.res, left+node.val+right)
        return max(left, right) + node.val