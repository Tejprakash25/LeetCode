class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        root = TrieNode()
        for word in products:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if len(node.words) < 3:
                    node.words.append(word)
        ans = []
        node = root
        for ch in searchWord:
            if node and ch in node.children:
                node = node.children[ch]
                ans.append(node.words)
            else:
                node = None
                ans.append([])
        return ans