class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string substring = "";
        generateParenthesis(n,n,substring,ans);
        return ans;
    }
    void generateParenthesis(int left, int right, string substring, vector<string> &s)
    {
        if(left>right) return;
        if(left == 0 && right == 0)
        {
            s.push_back(substring);
            return;
        }
        
        else
        {
            if(left>0) generateParenthesis(left-1,right, substring+'(',s);
            if(right>0) generateParenthesis(left,right-1, substring+')',s);
        }
    }
};
//利用set的不可重复性，在n-1的基础上，每发现一个左括号，就在后面加一个“()”，然后
//把set转成vector
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        set<string>res;
        if(n == 0)  res.insert("");
        else
        {
            vector<string>temp=generateParenthesis(n-1);
            for(auto a : temp)
            {
                for(int i=0;i<a.size();i++)
                {
                    if(a[i]== '(')
                    {
                        a.insert(a.begin()+1+i,'(');
                        a.insert(a.begin()+2+i,')');
                        res.insert(a);
                        a.erase(a.begin() + i + 1, a.begin() + i + 3);
                    }
                }
                res.insert("()"+a);
            }

        }
        return vector<string>(res.begin(),res.end());

    }
};
