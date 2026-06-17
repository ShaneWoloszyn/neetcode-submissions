# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # finds length of array
        temp = head
        i = 0
        while temp:
            i += 1
            temp = temp.next
    
        # target = # of the one to remove
        target = i - n

        # if target = 0, remove first
        if not target:
            return head.next
        
        # else go to and set the one and set it to the one ahead
        temp = head
        for i in range(target - 1):
            temp = temp.next
        
        if temp and temp.next and temp.next.next:
            temp.next = temp.next.next
        else:
            temp.next = None

        return head