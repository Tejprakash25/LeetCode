"""Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
(each edge is a pair of nodes), write a function to check whether these
 edges make up a valid tree."""

class solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False
            
            parent[rootY] = rootX
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False
            
        return True