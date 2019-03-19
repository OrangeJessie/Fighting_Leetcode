/*除了自身数组的乘积，首先考虑i前的成绩后和i之后的乘积，但是运行时间很长O(n^2)
*/
class Solution{
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans;
        for (int i=0;i<nums.size();i++)
        {
            int tmp=1;
            for(int j=0;j<i;j++)
            {
                tmp*=nums[j];
            }
            for(int k=i+1;k<nums.size();k++)
            {
                tmp*=nums[k];
            }
            ans.push_back(tmp);
        }
        return ans;
    }
};
/*改进，去掉一个循环，从前遍历数组，将前n项的乘积放进新数组的第n+1里面
两种方法不同之处在于是否借用新数组
*/
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        /*
        int n=nums.size();
        vector<int>ans(n);
        vector<int>fwd(n,1),bwd(n,1);
        for(int i=0;i<n-1;i++)
        {
            fwd[i+1]=nums[i]*fwd[i];
        }
        for(int i=n-1;i>0;i--)
        {
            bwd[i-1]=nums[i]*bwd[i];
        }
        for(int i=0;i<n;i++)
        {
            ans[i]=fwd[i]*bwd[i];   
        }
        return ans;
        */
        int n=nums.size();
        vector<int>ans(n,1);
        for(int i=1;i<n;i++)
        {
            ans[i]=ans[i-1]*nums[i-1];
        }
        int right=1;
        for(int i=n-1;i>=0;i--)
        {
            ans[i]*=right;
            right*=nums[i];
        }
        return ans;
    }
};
