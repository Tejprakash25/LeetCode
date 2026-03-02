"""
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence
 of two strings is a subsequence that is common to both strings."""


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        
        prev = [0]*(len(text2)+1)
        
        for c1 in text1:
            curr = [0]*(len(text2)+1)
            
            for j, c2 in enumerate(text2):
                if c1 == c2:
                    curr[j+1] = 1 + prev[j]
                else:
                    curr[j+1] = max(prev[j+1], curr[j])
            
            prev = curr
        
        return prev[-1]