# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def search(root, level):
            if not root:
                return
            
            if len(res) == level:
                res.append([])
            
            res[level].append(root.val)
            
            search(root.left, level + 1)
            search(root.right, level + 1)
        
        search(root, 0)

        ans = []
        for lists in res:
            ans.append(lists[-1])
        
        return ans