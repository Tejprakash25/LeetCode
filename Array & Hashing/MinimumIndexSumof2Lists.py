class Solution(object):
    def findRestaurant(self, list1, list2):

        hashmap = {}

        for i in range(len(list1)):
            hashmap[list1[i]] = i

        min_sum = float('inf')

        result = []

        for j in range(len(list2)):

            if list2[j] in hashmap:

                index_sum = j + hashmap[list2[j]]

                if index_sum < min_sum:

                    min_sum = index_sum

                    result = [list2[j]]

                elif index_sum == min_sum:

                    result.append(list2[j])

        return result