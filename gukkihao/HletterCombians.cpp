//回溯算法，还没有弄明白是个什么鬼，大概意思就是执行某一步走不通时返回上一步，然后选择其他的路走？
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        string dict []={"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};//把2-9的数字对应的字母存放在数组内，可以用map代替
        if(digits.empty()) return {};
        int level = 0;//表示digits的第level个字符
        string substring="";//每个子集字符串
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
            letterCombinationsDFS(digits, dict, level+1,temp+string(1,str[i]) ,ans);//string(1,str[i])应该是把str[i]转换成string类。
        }
    }
};
