/*
整数相除，得到的小数是无限循环小数或者整数
*/
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        int sign_1=numerator >= 0 ? 1 : -1;
        int sign_2=denominator>=0 ? 1 : -1;
        long long num= abs((long long)numerator);
        long long den= abs((long long)denominator);
        long long out=num/den;
        long long rem=num%den;
        unordered_map<long long, int> m;
        string ans=to_string(out);
        if(sign_1*sign_2==-1&&(out>0||rem>0)) ans="-"+ans;
        if(rem==0) return ans;
        ans+=".";
        string s="";
        int pos=0;
        while(rem!=0)
        {
            if(m.find(rem)!=m.end())
            {
                s.insert(m[rem],"(");
                s+=")";
                return ans+s;
            }
             m[rem] = pos;
            s += to_string((rem * 10) / den);
            rem = (rem * 10) % den;
            ++pos;
            
        }
        return ans + s;
    }
};
