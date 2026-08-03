# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeLen = 0
        cur = head

        while cur:
            nodeLen += 1
            cur = cur.next
        
        if nodeLen <= 1:
            return None
        
        if nodeLen - n == 0:
            return head.next
        
        cur = head
        for _ in range(nodeLen - n - 1):
            cur = cur.next
        
        cur.next = cur.next.next

        return head
