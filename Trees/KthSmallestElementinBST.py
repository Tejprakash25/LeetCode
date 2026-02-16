"""Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the 
nodes in the tree.
"""

class Solution:
    def kthSmallest(self, root, k):
        
        self.k = k
        self.result = None
        
        def inorder(node):
            if not node or self.result is not None:
                return
            
            inorder(node.left)
            
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            
            inorder(node.right)
        
        inorder(root)
        return self.result
