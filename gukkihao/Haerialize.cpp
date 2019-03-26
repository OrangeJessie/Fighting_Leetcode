class Codec {
public:
    string serialize(TreeNode* root) {
        if (!root) return "";
        ostringstream os;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode *t = q.front(); q.pop();
            if (t) {
            os << t->val << " ";
            q.push(t->left);
            q.push(t->right);
            } else {
                os << "# ";
            }
        }
        return os.str();
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data.empty()) return NULL;
        istringstream is(data);
        queue<TreeNode*> q;
        string val="";
        is>>val;
        TreeNode* res=new TreeNode(stoi(val)),*cur=res;
        q.push(cur);
        while(!q.empty())
        {
            TreeNode*t=q.front();q.pop();
            if(!(is>>val)) break;
            if(val!="#")
            {
                cur=new TreeNode(stoi(val));
                q.push(cur);
                t->left=cur;
            }
            if(!(is>>val)) break;
            if(val!="#")
            {
                cur=new TreeNode(stoi(val));
                q.push(cur);
                t->right=cur;
            }
        }
        return res;
    }
};

