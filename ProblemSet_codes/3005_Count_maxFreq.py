""" 
3005. Count Elements with Max Frequency

You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

 

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.
Example 2:

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
 
"""

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        word_freq = {}
        for num in nums:
            if num in word_freq:
                word_freq[num] += 1
            else:
                word_freq[num] = 1

        my_list_freq = []
        for value in word_freq.values():
            my_list_freq.append(value)

        max_freq = max(my_list_freq)
        return(sum([x for x in my_list_freq if x==max_freq]))

        


# Main
if __name__ == "__main__":
    nums = [1,2,2,3,1,4]
    print(Solution().maxFrequencyElements(nums)) # 4
    nums = [1,2,3,4,5]
    print(Solution().maxFrequencyElements(nums)) # 5
    
