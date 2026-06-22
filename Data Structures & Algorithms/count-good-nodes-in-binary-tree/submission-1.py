# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def check(node: TreeNode, maxVal) -> int:
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0

            maxVal = max(maxVal, node.val)
            res += check(node.left, maxVal)
            res += check(node.right, maxVal)
            return res
        
        return check(root, root.val)
        