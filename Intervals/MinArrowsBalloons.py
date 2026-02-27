"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows
"""

class Solution:
    def findMinArrowShots(self, points):
        
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        end = points[0][1]
        
        for start, finish in points[1:]:
            
            if start > end:
                arrows += 1
                end = finish
        
        return arrows