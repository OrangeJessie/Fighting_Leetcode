//从末尾开始比较,把较大的值放在nums1的最后值，然后当nums1或者Nums2比较完之后，将nums1或者nums2的未比较部分直接放进nums1的前面
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i=m-1,j=n-1,k=m+n-1;
        while(j>=0&&i>=0)
        {
            if(nums1[i]>nums2[j])
                nums1[k--]=nums1[i--];
            else
                nums1[k--]=nums2[j--];
        }
        while(j>=0)
        {
            nums1[k--]=nums2[j--];
        }
        return;
    }
};
