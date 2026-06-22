# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return 
        count = head
        i = 0
        while count:
            i += 1
            count = count.next

        cur = head
        n = i - n

        if n == 0:
            return cur.next
        
        while n > 1:
            n -= 1
            cur = cur.next
        
        cur.next = cur.next.next
        return head