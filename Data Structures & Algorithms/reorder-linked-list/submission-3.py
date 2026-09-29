# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        cur, prev = second, None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        first = head
        second = prev

        res = cur = ListNode()

        while second:
            cur.next = first
            cur = cur.next
            first = first.next

            cur.next = second
            cur = cur.next
            second = second.next
        
        cur.next = first

        head = res.next