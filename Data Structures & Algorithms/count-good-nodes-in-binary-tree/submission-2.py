# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        cnt = 1
        def dfs(node, max_value):
            nonlocal cnt
            if node.left:
                dfs(node.left, max(max_value, node.left.val))
                if node.left.val >= max_value:
                    cnt += 1
            if node.right:
                dfs(node.right, max(max_value, node.right.val))
                if node.right.val >= max_value:
                    cnt += 1
        dfs(root, root.val)
        return cnt