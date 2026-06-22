# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root: Optional[TreeNode]) -> List[Bool, int]:
            if not root:
                return [True, 0]
            
            root.left, root.right = dfs(root.left), dfs(root.right)
            print(root.left, root.right)

            if root.left[0] and root.right[0] and abs(root.left[1] - root.right[1]) <= 1:
                return [True, 1 + max(root.left[1], root.right[1])]
            return [False, max(root.left[0], root.right[0])]
        
        return dfs(root)[0]