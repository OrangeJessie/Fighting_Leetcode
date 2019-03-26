class Solution(object):
    # 动态规划
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = [1]
        num = [0, 1, 2]
        for i in range(3, n+1):
            new_candidate = (len(candidate)+1)**2
            if i >= new_candidate:
                candidate.append(new_candidate)
            subnum = 2**31-1
            for j in candidate:
                subnum = min(1+num[i-j], subnum)
            num.append(subnum)
        return num[n]

    # 四数定理
    def numSquares2(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4

        if n % 8 == 7:
            return 4

        a = 0
        while a**2 <= n:
            b = int((n - a**2)**0.5)
            if a**2 + b**2 == n:
                return (not not a) + (not not b)

            a += 1

        return 3
