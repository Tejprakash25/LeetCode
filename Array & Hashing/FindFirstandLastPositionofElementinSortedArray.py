class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def binary_search(target):
            left, right = 0, len(nums)

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        first = binary_search(target)

        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        last = binary_search(target + 1) - 1

        return [first, last]