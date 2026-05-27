# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        seen = [ListNode()]
        while head.next:
            if head.next in seen:
                return True    
            seen.append(head)
            head = head.next
        return False
