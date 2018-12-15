class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        i = 0
        length = len(prices)
        while i < length-1:
            if prices[i] < prices[i+1]:
                profit += prices[i+1] - prices[i]
            i += 1
        return profit


s = Solution()
price = [1, 2, 6, 5]
print(s.maxProfit(price))
