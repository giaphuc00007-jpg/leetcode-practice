# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while curr.next and curr.next.next:
            le = curr.next 
            chan = curr.next.next

            le.next = chan.next
            chan.next = le 
            curr.next = chan

            curr = le 
        return dummy.next