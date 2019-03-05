//利用迭代的方法进行递归遍历
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int>ans;
        if(!root) return ans;
        inorder(root,ans);
        return ans;
    }
    void inorderTraversal(TreeNode* root, vector<int> &nums)
    {
        if(!root) return nums;
        if(root->left) inorderTraversal(root->left,nums);
        nums.push_back(root->val);
        if(root->right) inorderTraversal(root->right,nums);
    }
};
//利用stack的先进先出原则，首先把根节点放进stack里面，然后一次把根节点的左节点也放进stack，如果左节点
//放完之后，那么先弹出栈顶的节点，并把弹出的节点值放进vector里面，再把右节点放进stack里面，依次操作，
//直到节点全都放进stack一遍并且stack里的节点全部弹出并把值保存在vector里面。
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> tmp;
        vector<int> ans;
        TreeNode*p=root;
        while(p||!tmp.empty()){
            if(p){
                tmp.push(p);
                p=p->left;
            }
            else {
                p=tmp.top();
                tmp.pop();
                ans.push_back(p->val);
                p=p->right;
            }
        }
        return ans;
    }
};