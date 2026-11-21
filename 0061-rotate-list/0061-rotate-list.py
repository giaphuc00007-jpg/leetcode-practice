# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        n = 0
        curr = head
        while curr:
            n += 1 
            curr = curr.next

        k = k % n
        while k > 0:
            curr= head 
            while curr:
                if curr and curr.next:
                    near_end = curr
                curr = curr.next
            end = near_end.next
            near_end.next = None
            end.next = head
            head = end
            k -= 1
        return head