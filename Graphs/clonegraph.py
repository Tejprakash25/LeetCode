"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.


"""

class Solution:
    def cloneGraph(self, node):
        
        if not node:
            return None
        
        visited = {}
        
        def dfs(curr):
            
            if curr in visited:
                return visited[curr]
            
            copy = Node(curr.val)
            visited[curr] = copy
            
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)