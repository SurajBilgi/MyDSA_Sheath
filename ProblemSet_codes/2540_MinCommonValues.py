""" 
2540. Min Common Values

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
"""

class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        common = nums1_set.intersection(nums2_set)
        if common:
            return(min(common))
        else:
            return(-1)
        
        # for num in nums1_set:
        #     if num in nums2_set:
        #         return(num)

# Main
if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [2,4]
    print(Solution().getCommon(nums1, nums2)) # 2
    nums1 = [1,2,3,6]
    nums2 = [2,3,4,5]
    print(Solution().getCommon(nums1, nums2)) # 2
