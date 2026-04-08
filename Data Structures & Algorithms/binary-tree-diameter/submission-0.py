# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = 0
        def dfs(node):
            nonlocal max_d
            res_left = dfs(node.left) if node.left else 0
            res_right = dfs(node.right) if node.right else 0
            max_d = max(max_d, res_left + res_right)
            return 1 + max(res_left, res_right)
        dfs(root)
        return max_d