"""Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees."""

class Solution:
    def isValidBST(self, root):
        return self.validate(root, float('-inf'), float('inf'))
    
    
    def validate(self, node, low, high):
        
        if not node:
            return True
        
        if not (low < node.val < high):
            return False
        
        left_valid = self.validate(node.left, low, node.val)
        
        right_valid = self.validate(node.right, node.val, high)
        
        return left_valid and right_valid
