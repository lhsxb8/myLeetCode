# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fastnode = head
        slownode = head

        while fastnode is not None and fastnode.next is not None:
            fastnode = fastnode.next.next
            slownode = slownode.next
        
        return slownode