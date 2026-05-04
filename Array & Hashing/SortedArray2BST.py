# THIS SOLUTION IS OPTIMIZED VERSION OF SOLVED BEFORE 
# Leetcode problem 108. Convert Sorted Array to Binary Search Tree

class Solution(object):
    def buildBST(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums, left, mid - 1)
        root.right = self.buildBST(nums, mid + 1, right)
        return root
    
    def sortedArrayToBST(self, nums):
        return self.buildBST(nums, 0, len(nums) - 1)