# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []

        for head in lists:
            while head:
                arr.append(head.val)
                head = head.next
        arr = sorted(arr)

        ans = head = ListNode
        if len(arr) == 0:
            return
        for n in arr:
            head.next = ListNode(n)
            head = head.next
        
        return ans.next