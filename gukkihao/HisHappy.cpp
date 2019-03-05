/*
class Solution {
public:
    bool isHappy(int n) {
        set <int> s;
        while(n!=1)
        {
            int t=0;
            while(n)
            {
                t+=(n%10)*(n%10);
                n/=10;
            }
            n=t;
            if(s.count(n)) break;
            else s.insert(n);
        }
        return n==1;
    }
};
*/
class Solution {
    public:
    bool isHappy(int n) {
        while(n!=1&&n!=4)
        {
            int t=0;
            while(n)
            {
                t+=(n%10)*(n%10);
                n/=10;
            }
            n=t;
        }
        return n==1;
    }
};
