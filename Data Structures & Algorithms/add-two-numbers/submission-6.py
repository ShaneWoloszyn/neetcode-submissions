# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = head = ListNode()
        carry = 0

        while l1 or l2:
            cur = carry
            carry = 0
            if l1:
                cur += l1.val
                l1 = l1.next
            if l2:
                cur += l2.val
                l2 = l2.next
            if cur >= 10:
                carry += cur // 10
            
            cur %= 10
            head.next = ListNode(cur)
            head = head.next

        if carry != 0:
            head.next = ListNode(carry)
        
        return res.next
        
    
        