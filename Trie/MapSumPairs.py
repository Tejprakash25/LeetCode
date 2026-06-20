class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.mp = {}

    def insert(self, key, val):
        delta = val - self.mp.get(key, 0)
        self.mp[key] = val
        node = self.root

        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.score += delta

    def sum(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.score