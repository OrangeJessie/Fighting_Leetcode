/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 //中序遍历，先遍历整个二叉搜索树把节点放进stack里面，然后依次取出k个节点
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int cnt=0;
        stack <TreeNode*> s;
        TreeNode*cur=root;
        while(cur||!s.empty())
        {
            while(cur)
            {
                s.push(cur);
                cur=cur->left;               
            }
            cur=s.top();
            s.pop();
            ++cnt;
            if(cnt==k) return cur->val;
            cur=cur->right;
        }
        return 0;
    }
};
