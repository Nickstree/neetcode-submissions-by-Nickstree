# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(node_a, node_b):
            if node_a and node_b and node_a.val == node_b.val:
                return same_tree(node_a.left, node_b.left) and same_tree(node_a.right, node_b.right)             
            elif not node_a and not node_b:
                return True
            else:
                return False 
        if not subRoot:
            return True
        elif not root:
            return False
        else:
            if same_tree(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    