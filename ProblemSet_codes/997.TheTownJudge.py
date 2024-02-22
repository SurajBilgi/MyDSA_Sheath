""" 
997. Find the Town Judge.

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

"""
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust)==0 and n==1:
            return 1
        my_trust = {}
        for tst in trust:
            try:
                if len(my_trust)==0:
                    my_trust[tst[1]]=[tst[0]]
                else:
                    my_trust[tst[1]].append(tst[0])
            except:
                my_trust[tst[1]] = [tst[0]]

        my_key = []
        for key, values in my_trust.items():
            # print(key)
            # print(values)
            if key in values:
                # values.remove(key)
                pass
            
            if len(values)==n-1:
                my_key.append(key)
                # pass
        
        for key, values in my_trust.items():
            for k in my_key:
                if k in values:
                    my_key.remove(k)

        if len(my_key) == 1:
            return my_key[0]
        
        return -1


run = Solution()
n=3
trust = [[1,3],[2,3],[3,1]]
print(run.findJudge(n,trust))