# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLen = 0
        cur = head
        while cur:
            listLen += 1
            cur = cur.next
        
        toDelete = listLen - n

        if toDelete == 0:
            return head.next
        

        cur = head

        for _ in range(toDelete - 1):
            cur = cur.next
        
        cur.next = cur.next.next if cur.next.next else None

        return head