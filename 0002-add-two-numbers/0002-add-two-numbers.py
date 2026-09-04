# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0)
        curr = dummy 
        du = 0 
        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry = val1 + val2 + du 
            save = carry %10 
            du = carry//10
            curr.next = ListNode(save)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        
        if du > 0:
            curr.next = ListNode(du)
        return dummy.next 
