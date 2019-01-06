class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(!root) return;
        if(root->left) root->left->next=root->right;
        if(root->right) root->right->next=root->next?root->next->left:NULL;
        connect(root->left);
        connect(root->right);
    }
};

class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(!root) return;
        queue<TreeLinkNode*>q;
        q.push(root);
        q.push(NULL);
        while(!q.empty())
        {
            TreeLinkNode*cur=q.front();
            q.pop();
            if(cur)
            {
                cur->next=q.front();
                if(cur->left) q.push(cur->left);
                if(cur->right) q.push(cur->right);
            }
            else
            {
                if(q.size()==0||q.front()==NULL) return;
                q.push(NULL);
            }
        }
    }
};

class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(!root) return;
        TreeLinkNode*start=root,*cur=NULL;
        while(start->left)
        {
            cur=start;
            while(cur)
            {
                cur->left->next=cur->right;
                if(cur->next) cur->right->next=cur->next->left;
                cur=cur->next;
            }
            start=start->left;
        }
        
    }
};
