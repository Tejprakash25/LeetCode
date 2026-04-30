class Solution(object):
    def removeElement(self, nums, val):
        a = 0
        for i in nums:
            if i != val:
                nums[a] = i
                a += 1
        
        return a