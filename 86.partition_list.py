"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        small_dummy = ListNode(-1)
        large_dummy = ListNode(-1)

        prev = dummy
        small_prev = small_dummy
        large_prev = large_dummy
        while prev.next:
            curr = prev.next
            if curr.val < x:
                small_prev.next = curr
                small_prev = small_prev.next
            else:
                large_prev.next = curr
                large_prev = large_prev.next
            prev = prev.next
        large_prev.next = None
        small_prev.next = large_dummy.next
        return small_dummy.next