""" 
1481. Least Number of Unique Integers after K removal

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

"""

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        freq = sorted(freq.values())

        i = 0
        while k!=0:
            if freq[i]!=0:
                k-=1
                freq[i]=freq[i]-1
            else:
                i+=1

        result_list = [x for x in freq if x !=0]
        return len(result_list)
        

run = Solution()
arr = [5,5,4]
k = 1
print(run.findLeastNumOfUniqueInts(arr,k))