class Solution:
    def palindromePairs(self, words):

        mp = {word:i for i, word in enumerate(words)}
        res = []

        for i, word in enumerate(words):

            for j in range(len(word)+1):

                left = word[:j]
                right = word[j:]

                if left == left[::-1]:

                    rev = right[::-1]

                    if rev in mp and mp[rev] != i:
                        res.append([mp[rev], i])

                if j != len(word) and right == right[::-1]:

                    rev = left[::-1]

                    if rev in mp and mp[rev] != i:
                        res.append([i, mp[rev]])

        return res