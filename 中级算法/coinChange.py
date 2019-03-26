# 零钱兑换
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
# 如果没有任何一种硬币组合能组成总金额，返回 -1。
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1


class Solution(object):
    # 动态规划
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount or not coins:
            return -1
        ways = [2**31-1]*(amount+1)
        for i in range(1, amount+1):
            for j in coins:
                if i-j < 0:
                    subway = 2**31-1
                elif i-j == 0:
                    subway = 1
                else:
                    subway = 1 + ways[i-j]
                if subway < ways[i]:
                    ways[i] = subway
        if ways[amount] == 2**31-1:
            return -1
        return ways[amount]

    # 深度遍历
    def coinChange2(self, coins, amount):
        coins.sort(reverse=True)                        # 硬币从大到小排序
        len_coins, self.result = len(coins), amount+1

        def countCoins(index, target, count):
            if not target:
                self.result = min(self.result, count)

            for i in range(index, len_coins):                           # 每一步 每一种硬币都要选择
                if coins[i] <= target < coins[i]*(self.result - count):        # 剪枝 当前硬币，用比上一次硬币数少的硬币能达到目标
                    countCoins(i, target - coins[i], count+1)

        countCoins(0, amount, 0)
        return -1 if self.result > amount else self.result


s = Solution()
s.coinChange2([1, 6, 10], 22)
