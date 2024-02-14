""" 
836. Rectangle Overlap

An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

 

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Example 3:

Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false
 

"""


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1,y1,x2,y2 = rec1
        rec2_pt = [(rec2[0],rec2[1]),(rec2[2],rec2[3]),(rec2[2],rec2[1]),(rec2[0],rec2[3])]
        print(rec2_pt)
        for x,y in rec2_pt:
            if x1 < x < x2 and y1 < y < y2:
                return True

        return False




run = Solution()
rec1 = [7,8,13,15]
rec2 = [10,8,12,20]
print(run.isRectangleOverlap(rec1,rec2))