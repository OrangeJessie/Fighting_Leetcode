//时间复杂度O(n)
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans=INT_MIN,cursum=0;
        for(int num : nums)
        {
            cursum=max(num,num+cursum);
            ans=max(ans,cursum);
        }
        return ans;
        
    }
};
//分治法，采用类似于二分法，将数组分为两段，然后再分别计算左右子段的最大
//子序列和，再从中间向左右寻找最大子序和
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.empty()) return 0;//判断数组是否为空
        return maxSubArray(nums,0,(int)nums.size()-1);//size()方法返回一个size_t类型，需要进行强制类型转换

    }
    int maxSubArray(vector<int> & nums,int left,int right)
    {
        if(nums.empty()) return 0;
        if(left>=right) return nums[left];//递归结束条件
        int mid=left+(right-left)/2;
        int lmax=maxSubArray(nums,left,mid-1);//计算左边子序最大序列和，注意mid-1
        int rmax=maxSubArray(nums,mid+1,right);//计算右边子序最大序列和，注意mid+1
        int mmax=nums[mid],cursum=mmax;//mmax=nums[mid]，这里计算到了mid，其他地方不用是为了避免重复计算
        for(int i=mid-1;i>=0;i--)//有中间点向左边搜索
        {
            cursum+=nums[i];
            mmax=max(mmax,cursum);
        }
        cursum=mmax;
        for(int i=mid+1;i<=nums.size()-1;i++)//由中间点向右边搜索
        {
            cursum+=nums[i];
            mmax=max(mmax,cursum);
        }
        return max(mmax,max(lmax,rmax));//返回三者最大值
    }
};
