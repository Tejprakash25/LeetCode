"""
Given two integer arrays preorder and inorder where preorder is the 
preorder traversal of a binary tree and inorder is the inorder traversal 
of the same tree, construct and return the binary tree.
"""

class Solution:
    def buildTree(self, preorder, inorder):
        
        index_map = {val: i for i, val in enumerate(inorder)}
        
        preorder_iter = iter(preorder)
        
        def build(left, right):
            if left > right:
                return None
            
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            mid = index_map[root_val]
    
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, len(inorder) - 1)

        