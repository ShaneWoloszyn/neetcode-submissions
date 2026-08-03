# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def same(l, r):
            if not l and not r:
                return True
            elif not l or not r:
                return False
            
            if l.val != r.val:
                return False
            
            return same(l.right, r.right) and same(l.left, r.left)
        
        return same(p, q)