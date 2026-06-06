class Solution(object):
    def buildArray(self, target, n):

        ans = []
        j = 0

        for num in range(1, n + 1):

            ans.append("Push")

            if num == target[j]:
                j += 1

                if j == len(target):
                    break

            else:
                ans.append("Pop")

        return ans