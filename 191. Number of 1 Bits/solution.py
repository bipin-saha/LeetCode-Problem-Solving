#Problem
#https://leetcode.com/submissions/detail/1312746920/

#Solution
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        binlst = []
        if n == 0:
            return n
        else:
            while n > 0:
                div = n % 2
                n = n // 2
                if div == 1:
                    binlst.append(div)
            
            return len(binlst)  