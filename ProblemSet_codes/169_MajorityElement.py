"""
169. Majority Element
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

"""

from collections import Counter
 
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)

        for ky,fq in freq.items():
            if fq>(len(nums)//2):
                return ky


run = Solution()
nums = [2,2,1,1,1,2,2]
print(run.majorityElement(nums))