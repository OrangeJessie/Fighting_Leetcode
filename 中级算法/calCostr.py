class Solution():
    def calCost(self, n, values):
        if not n:
            return 0
        cost = 0
        remain = 0
        for i in range(n):
            cost += abs(remain)
            remain += values[i]
        return cost

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    s = Solution()
    print(s.calCost(n, values))
