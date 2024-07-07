#Problem
#https://leetcode.com/problems/plus-one/submissions/1312990129/

#Solution
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ""
        for element in digits:
            num = num + str(element)
 
        return list(map(int, (str(int(num) + 1))))