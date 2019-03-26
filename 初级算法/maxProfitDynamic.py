class Solution(object):
    # 40ms
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if days <= 1:
            return 0
        r = [0]
        minimum = [2**32-1]
        for i in range(1, days):
            minimum.append(min(minimum[i-1], prices[i-1]))
            profit = max(r[i-1], prices[i]-minimum[i])
            r.append(profit)
        return max(r)

    # 24ms
    def maxProfit2(self, prices):
        iCurrentMax = 0
        iFinalMax = 0
        for i in range(len(prices) - 1):
            iCurrentMax += prices[i + 1] - prices[i]
            if iCurrentMax < 0:                 # 保证买入是最小的
                iCurrentMax = 0
            if iCurrentMax > iFinalMax:
                iFinalMax = iCurrentMax
        return iFinalMax

    # 28ms
    def maxProfit3(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        start = prices[0]
        profit = 0
        for ele in prices[1:]:
            if ele > start:
                if ele - start > profit:
                    profit = ele - start
            if ele <= start:
                start = ele
        return profit
