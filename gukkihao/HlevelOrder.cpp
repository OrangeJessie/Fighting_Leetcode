/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//迭代方法解决，主要思路是广度遍历搜索，建立一个列表利用其先进先出的性质把根节点
//存储起来然后再扎到跟节点的两个左右节点，再把根节点的给踢出去就找到了下一层的值
//
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int> > res;
        if(!root) return res;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty())
        {
            vector<int> onelevel;
            int len=q.size();
            for(int i=0;i<len;i++)
            {
                TreeNode* node=q.front();
                q.pop();
                onelevel.push_back(node->val);
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }
            res.push_back(onelevel);
        }
        return res;
        
    }
};
//递归方法解决
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int> > res;
        levelOrder(root,0,res);
        return res;
    }
    void levelOrder(TreeNode* root,int level,vector<vector<int> > &vec)
    {
        if(!root) return;
        if(vec.size()==level) vec.push_back({});
        vec[level].push_back(root->val);
        if(root->left) levelOrder(root->left,level+1,vec);
        if(root->right) levelOrder(root->right,level+1,vec);
    }
};
