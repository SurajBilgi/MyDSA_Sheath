""" 
201. BITWISE AND of Number Range

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
 


"""




class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        res = 0
        while left<right:
            left = left >> 1
            right = right >> 1
            res += 1

        return left << res
    

run = Solution()
left = 5
right = 7
print(run.rangeBitwiseAnd(left,right))

        
