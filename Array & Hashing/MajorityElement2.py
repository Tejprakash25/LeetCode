class Solution(object):
    def majorityElement(self, nums):
        cd1 = cd2 = None
        c1 = c2 = 0

        for x in nums:
            if cd1 == x:
                c1+=1
            elif cd2 == x:
                c2+=1
            elif c1 == 0:
                cd1, c1 = x, 1
            elif c2 == 0:
                cd2, c2 = x, 1
            else:
                c1-=1
                c2-=1
        
        return [c for c in (cd1, cd2)
                if c is not None and nums.count(c) > len(nums) // 3]