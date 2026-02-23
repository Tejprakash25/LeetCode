"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


"""

from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) != numCourses:
            return []
        
        return order