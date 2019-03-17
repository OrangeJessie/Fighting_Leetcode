/*
采用栈，把数组的数字依次放入栈里面，再依次取出两个数字，并依次选取一个符号
*/
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        if(tokens.size()==1) return stoi(tokens[0]);
        stack <int> st;
        for(int i=0;i<tokens.size();i++)
        {
            if(tokens[i]!="+"&&tokens[i]!="-"&&tokens[i]!="*"&&tokens[i]!="/")
                st.push(stoi(tokens[i]));
            else
            {
                int s1=st.top();st.pop();
                int s2=st.top();st.pop();
                if(tokens[i]=="+") st.push(s2+s1);
                if(tokens[i]=="-") st.push(s2-s1);
                if(tokens[i]=="*") st.push(s2*s1);
                if(tokens[i]=="/") st.push(s2/s1);
            }
        }
        return st.top();
    }
};
