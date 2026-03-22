"""
Given a collection of candidate numbers (candidates) and a target number 
(target), find all unique combinations in candidates where the candidate 
numbers sum to target.
Each number in candidates may only be used once in the combination.
"""

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(list(current))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                if i > start and candidates[i] == candidates[i-1]:
                    continue

                current.append(candidates[i])
                backtrack(i+1, current, remaining - candidates[i])
                current.pop()
        
        backtrack(0, [], target)
        return result
