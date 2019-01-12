//先找出最小值，然后再做差，把较大的差值存起来，不能用两层循环遍历，超时
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty()) return 0;
        int ans=0, buy=INT_MAX;
        for(int price : prices)
        {
            buy=min(buy,price);
            ans=max(ans,price-buy);
        }
        return ans;
    }
};
