""" 
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return nums1_set.intersection(nums2_set)
        
# Main
if __name__ == '__main__':
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(Solution().intersection(nums1, nums2)) # [2]
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(Solution().intersection(nums1, nums2)) # [9,4]

