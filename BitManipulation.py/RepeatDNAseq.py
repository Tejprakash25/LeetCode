"""
Given a string s representing a DNA sequence, return all 10-letter-long sequences that occur more than once.

DNA only contains:

'A', 'C', 'G', 'T'"""

class Solution:
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        
        mapping = {
            'A': 0,
            'C': 1,
            'G': 2,
            'T': 3
        }
        
        seen = set()
        repeated = set()
        
        hash_val = 0
        
        for i in range(len(s)):
            hash_val = ((hash_val << 2) | mapping[s[i]]) & ((1 << 20) - 1)
            
            if i >= 9:
                if hash_val in seen:
                    repeated.add(s[i-9:i+1])
                else:
                    seen.add(hash_val)
        
        return list(repeated)




