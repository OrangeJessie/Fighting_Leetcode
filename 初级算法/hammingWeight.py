class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)[2:]
        count = 0
        for i in s:
            if i == '1':
                count += 1
        return count

    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp=n
        res=0
        while(temp):
            res+=temp%2
            temp=temp/2
        return res
