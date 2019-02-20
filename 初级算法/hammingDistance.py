class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        sx = '0'
        sy = '0'
        count = 0
        while x > 0:
            sx = str(x % 2) + sx
            x = x//2
        while y > 0:
            sy = str(y % 2) + sy
            y = y//2
        lx = len(sx)
        ly = len(sy)
        if lx > ly:
            diff = lx - ly
            for i in range(diff):
                sy = '0' + sy
            for i in range(lx):
                if sx[i] != sy[i]:
                    count += 1
        elif ly > lx:
            diff = ly - lx
            for i in range(diff):
                sx = '0' + sx
            for i in range(ly):
                if sx[i] != sy[i]:
                    count += 1
        else:
            for i in range(ly):
                if sx[i] != sy[i]:
                    count += 1
        return count
