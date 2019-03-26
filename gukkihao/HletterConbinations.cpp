//回溯算法还不是很懂，大意是走到当前步骤时，如果结果不符合要求，那么返回上一步，
//找寻新的下一步
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        string dict []={"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};//把数字对应的字母放进string数组内
        if(digits.empty()) return {};
        int level = 0;//表示当前digits内的第level个数字
        string substring="";//组成ans的每个组合string
        vector<string>ans;
        letterCombinationsDFS(digits,dict,level,substring,ans);
        return ans;
    }
    void letterCombinationsDFS(string digits, string dict [], int level,string temp, vector<string>&ans)
    {
        if(level == digits.size()) 
        {
            ans.push_back(temp);
            return;
        }
        string str=dict[digits[level]-'2'];
        for(int i=0;i<str.size();i++)
        {
            letterCombinationsDFS(digits, dict, level+1,temp+string(1,str[i]) ,ans);
        }
    }
};
