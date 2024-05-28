""" 
1208. Get Equal Substrings Within Budget

You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.


Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.

Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to charactor in t, so the maximum length is 1.

"""

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        lens = len(s)
        diff = [abs(ord(s[i])-ord(t[i])) for i in range(lens)]
        # print(diff)

        left = 0
        right = 0
        max_length = 0
        current_cost = 0
        while right < lens:
            current_cost += diff[right]
            while current_cost > maxCost:
                current_cost -= diff[left]
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1  

        return max_length
    
        


run = Solution()
s = "abcd"
t = "bcdf"
maxCost = 3

print(run.equalSubstring(s,t,maxCost))