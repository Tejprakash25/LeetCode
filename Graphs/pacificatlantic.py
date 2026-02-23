"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c)
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""

class Solution:
    def pacificAtlantic(self, heights):
        
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited):
            
            visited.add((r, c))
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
                    
                    dfs(nr, nc, visited)
        
        
      
        for r in range(rows):
            dfs(r, 0, pacific)              
            dfs(r, cols - 1, atlantic)     
        
        for c in range(cols):
            dfs(0, c, pacific)             
            dfs(rows - 1, c, atlantic)     
        
        return list(pacific & atlantic)