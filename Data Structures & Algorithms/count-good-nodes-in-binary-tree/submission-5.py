# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def search(root, curMax):
            if not root:
                return
            nonlocal res
            if curMax <= root.val:
                res += 1
                curMax = root.val
            
            search(root.left, curMax)
            search(root.right, curMax)
        
        search(root, -float('inf'))

        return res