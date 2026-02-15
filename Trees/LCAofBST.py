"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) 
node of two given nodes in the BST. According to the definition of LCA on 
Wikipedia: “The lowest common ancestor is defined between two nodes p and q as 
the lowest node in T that has both p and q as descendants (where we allow a node
 to be a descendant of itself).”
"""

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        if p.val < root.val and q.val < root.val:
            return(self.lowestCommonAncestor(root.left, p, q))
        
        if p.val > root.val and q.val < root.val:
            return(self.lowestCommonAncestor(root.right, p, q))

        return root
        