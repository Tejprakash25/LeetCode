"""
127. Word Ladder
Given two words, beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:
- Only one letter can be changed at a time.
- Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
"""

from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        L = len(beginWord)
        pattern = defaultdict(list)
        
        for word in wordSet:
            for i in range(L):
                pattern[word[:i] + "*" + word[i+1:]].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            word, level = queue.popleft()
            
            for i in range(L):
                key = word[:i] + "*" + word[i+1:]
                
                for nei in pattern[key]:
                    if nei == endWord:
                        return level + 1
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, level + 1))
                
                pattern[key] = []
        
        return 0