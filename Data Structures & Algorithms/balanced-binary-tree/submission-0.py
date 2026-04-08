# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if not node:
                return 0, True
            else:
                h_left, is_balanced_left = dfs(node.left)
                h_right, is_balanced_right = dfs(node.right)
                is_balanced = is_balanced_left and is_balanced_right and abs(h_left - h_right) <= 1
                return 1 + max(h_left, h_right), is_balanced

        _, is_balanced = dfs(root)
        return is_balanced