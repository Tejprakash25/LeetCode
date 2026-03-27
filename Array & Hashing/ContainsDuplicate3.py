"""
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

    i != j,
    abs(i - j) <= indexDiff.
    abs(nums[i] - nums[j]) <= valueDiff, and

Return true if such pair exists or false otherwise."""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0:
            return False

        bucket = {}
        w = t + 1

        for i in range(len(nums)):
            num = nums[i]
            b = num // w

          
            if b in bucket:
                return True

        
            if b - 1 in bucket and abs(num - bucket[b - 1]) <= t:
                return True
            if b + 1 in bucket and abs(num - bucket[b + 1]) <= t:
                return True

            bucket[b] = num

            
            if i >= k:
                old_b = nums[i - k] // w
                del bucket[old_b]

        return False