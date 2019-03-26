# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        start = 1
        mid = (n+start)//2
        dif = n-start
        while dif > 1:
            if isBadVersion(mid):
                n = mid
            else:
                start = mid
            mid = (n+start)//2
            dif = n-mid
        if isBadVersion(mid):
            return mid
        else:
            return mid+1

    def firstBadVersion2(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


