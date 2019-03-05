/*
//调用系统sort函数进行排序，然后再找到第k个大的数值即可
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        while(nums.size()!=n-k+1)
        {
            nums.pop_back();
        }
        return nums.back();
        
    }
};
*/
/*
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        return nums[nums.size()-k];
    }
};
*/
//快排应用，还没怎么理解，好像并没有完全排序
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int left=0,right=nums.size()-1;
        while(true)
        {
            int pos=quicksort(nums,left,right);
            if(pos==k-1) return nums[pos];
            else if(pos>k-1) right=pos-1;
            else left=pos+1;
        }
    }
    int quicksort(vector<int>& nums, int left,int right)
    {
        int pivot=nums[left], l=left+1, r=right;
        while(l<=r)
        {
            if(nums[l]<pivot&&nums[r]>pivot)
            {
                //nums[l]=nums[l]+nums[r];
                //nums[r]=nums[l]-nums[r];
                //nums[l]=(nums[l]-nums[r])/2;
                //nums[r]=nums[r]+nums[l];
                //l++;r--;
                swap(nums[r--],nums[l++]);
            }
            if(nums[l]>=pivot) l++;
            if(nums[r]<=pivot) r--;
        }
        swap(nums[left],nums[r]);
        return r;
        
    }
};
