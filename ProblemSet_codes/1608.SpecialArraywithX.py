""" 
1608. Special Array With X Elements Greater Than or Equal X

You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Example 2:

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.

Example 3:

Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.



"""


class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        freq = [0] * (N + 1)
        
        for num in nums:
            freq[min(N, num)] += 1
        # print(freq)
        num_greater_than_or_equal = 0
        for i in range(N, 0, -1):
            num_greater_than_or_equal += freq[i]
            # print(num_greater_than_or_equal,i)
            if num_greater_than_or_equal == i:
                return i
            # print(freq[i])


run = Solution()
nums = [3,5,1,1,6,7,8,9]
print(run.specialArray(nums))
