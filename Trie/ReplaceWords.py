class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def replaceWords(self, dictionary, sentence):
        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
        res = []
        for word in sentence.split():
            node = root
            for ch in word:
                if ch not in node.children or node.word:
                    break
                node = node.children[ch]
            res.append(node.word if node.word else word)
        return " ".join(res)