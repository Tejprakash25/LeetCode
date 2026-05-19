class Solution(object):
    def splitArray(self, nums, m):

        left = max(nums)
        right = sum(nums)

        result = right

        while left <= right:

            mid = (left + right) // 2

            partitions = 1
            current_sum = 0

            for num in nums:

                if current_sum + num > mid:

                    partitions += 1
                    current_sum = num

                else:
                    current_sum += num

            if partitions <= m:

                result = mid
                right = mid - 1

            else:
                left = mid + 1

        return result