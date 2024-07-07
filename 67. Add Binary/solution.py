#Problem
#https://leetcode.com/problems/add-binary/submissions/1312957143/

#Solution
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a, 2) + int(b, 2), 'b')