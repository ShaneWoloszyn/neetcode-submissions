# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def listToRevNumber(head: Optional[ListNode]) -> int:
            res = 0
            i = 1
            while head:
                res += head.val * i
                i *= 10
                head = head.next

            return res
        
        tot = str(listToRevNumber(l1) + listToRevNumber(l2))
        head = cur = ListNode()
        for t in tot[::-1]:
            cur.next = ListNode(t)
            cur = cur.next
        
        return head.next
        