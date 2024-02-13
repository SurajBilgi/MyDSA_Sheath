""" 
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

"""



from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        freq = Counter(s)

        # print(freq)
        for i in range(len(s)):
            if freq[s[i]]==1:
                return i 
            
        return -1




run = Solution()
s = "loveleetcode"
print(run.firstUniqChar(s))