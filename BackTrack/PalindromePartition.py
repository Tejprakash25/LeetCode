"""
Given a string s, partition it such that every substring of the partition 
is a palindrome. Return all possible palindrome partitionings.
Example: s = "aab" → [["a","a","b"], ["aa","b"]]
"""

class Solution:
    def partition(self, s):
        result = []

        def dfs(start, current):
            if start == len(s):
                result.append(list(current))
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub == sub[::-1]:
                    dfs(end, current + [sub])

        dfs(0, [])
        return result