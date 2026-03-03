"""
91. Decode Ways
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2""
...'Z' -> "26""
To decode an encoded message, all the digits must be grouped then mapped back into letters using the 
reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:"""


class Solution:
    def numDecodings(self, s):
        
        if not s or s[0] == '0':
            return 0
        
        prev2 = 1
        prev1 = 1 
        
        for i in range(1, len(s)):
            current = 0
            if s[i-1] != '0':
                current += prev1
            
            two = int(s[i-2:i])
            if 10 <= two <= 26:
                current += prev2

            prev2 = prev1
            prev1 = current
        
        return prev1
    

