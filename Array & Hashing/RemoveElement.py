class Solution(object):
    def searchInsert(self, nums, target):
        for i, v in enumerate(nums):
            if target <= v:
                return i
            
        return len(nums)