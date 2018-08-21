"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        node = head
        length = 0
        while node:
            node = node.next
            length += 1

            self.curr = head
            return self._sortedListToBST(0, length - 1)

    def _sortedListToBST(self, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        left = self._sortedListToBST(left, mid - 1)
        root = TreeNode(self.curr.val)
        root.left = left
        self.curr = self.curr.next
        root.right = self._sortedListToBST(mid + 1, right)
        return root