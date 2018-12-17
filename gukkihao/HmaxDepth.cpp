/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 //方法一: 利用层序遍历二叉树的所有层
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        int cnt=0;
        queue <TreeNode*> q;//初始化一个队列，先进先出
        q.push(root);//把第一个根节点放入队列
        while(!q.empty())
        {
            ++cnt;
            int n=q.size();//队列长度
            for (int i=0;i<n;i++)
            {
                TreeNode* t = q.front();
                q.pop();//去掉同一层的某个值,如果这一层只有一个值，那么queue的值为1，
                if(t->left) q.push(t->left);//把根节点的左右节点分别放进队列
                if(t->right) q.push(t->right);
            }
        }
        return cnt;
    }
};
//主要思想就是把根节点的左右节点放入队列中，然后再取出一个，终止条件是队列内的元素全部被取出也就完成了层序遍历
//方案二: 利用递归的思想，在树经常用
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};
//深度遍历