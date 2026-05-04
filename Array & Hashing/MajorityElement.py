class Solution(object):
    def majorityElement(self, nums):
        element = None
        count = 0

        for i in nums:
            if count == 0:
                element = i
            if i == element:
                count+=1
            else:
                count-=1
        return element