# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        val = 0
        while l1 or l2:
            if l1 and l2:
                val += (l1.val + l2.val) * i
                l1, l2 = l1.next, l2.next
            elif l1:
                val += l1.val * i
                l1 = l1.next
            else:
                val += l2.val * i
                l2 = l2.next
            i *= 10
        arr = list(''.join(reversed(str(val))))
        temp = head = ListNode()
        for i in range(len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
        
        return head.next