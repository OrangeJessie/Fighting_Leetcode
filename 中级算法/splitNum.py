class Solution:
    def splitNum(self, n, k):
        if not n:
            return 0
        ln = [n]
        count = 0
        while k:
            k -= 1
            count += 1
            newln = []
            for i in ln:
                newln.append(i // 2)
                newln.append(i-i//2)
            while 1:
                if 1 in newln:
                    count += 1
                    lenln = len(newln)
                    newnew = []
                    for j in range(lenln):
                        if newln[j] != 1:
                            newnew.append(newln[j]-1)
                    newln = newnew
                else:
                    break
            ln = newln
        if ln:
            count += max(ln)
        print(count)


import sys
if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    n = values[0]
    k = values[1]
    s = Solution()
    s.splitNum(n, k)
