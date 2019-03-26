//主要利用思想,二分法，高度平衡二叉搜索树（个高度平衡二叉树是指一个二叉树每个节点 
//的左右两个子树的高度差的绝对值不超过 1）
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        int len=nums.size()-1;
        return sortedArrayToBST(nums,0,len);
    }
    TreeNode* sortedArrayToBST(vector<int>&nums,int left,int right)
    {
        if(right<left) return NULL;
        int mid=(left+right)/2;
        TreeNode* cur=new TreeNode(nums[mid]);
        cur->left=sortedArrayToBST(nums,left,mid-1);
        cur->right=sortedArrayToBST(nums,mid+1,right);
        return cur;
    }
};